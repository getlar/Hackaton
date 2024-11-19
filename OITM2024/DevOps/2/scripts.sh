1.

For example, when princess /run calls lucky /run, it could produce the following two lines:

2024-09-27 12:22:53.841 INFO    --- [       princess] [274e0a9a-9bf6-4fbd-917f-53a0a7630780] [a592fdd0-9843-43a0-a9ed-606dcb727bd7] /run : I will invite Lucky
2024-09-27 12:22:53.856 INFO    --- [          lucky] [274e0a9a-9bf6-4fbd-917f-53a0a7630780] [4dec66f7-93e9-4544-9665-0c68b840435c] /run : running is fun
Where trace IDs are the same (because they are part of the same call chain), but the request IDs are different.

After understanding this, we should filter for rows with the service name princess, and the endpoint /invite-to-play. In the result, we should count the unique request IDs.

We could do all this with a dedicated log analyzer tool (for example, New Relic, Elastic Stack, Logz.io, Datadog, Dynatrace, or Splunk to name a few). Or, a few piped shell commands can also do the trick:

cat megmerettetes.log | \
awk '{print $6 " " $8 " " $9}' | \
grep "princess]" | \
awk '{print $2 " " $3}' | \
grep "/invite-to-play" | \
awk '{print $1}' | \
sort | \
uniq | \
wc -l

2.

The base idea is the same here: find all the unique calls for princess /invite-to-play. But instead of counting them, we need to find the first and last timestamp for every request ID. From that, we can calculate the execution time of every request. Then calculating their average is straightforward.

Since it's a bit more complex task, it's hard to solve using shell commands (but not impossible.) Using a dedicated tool or a higher-level language (like Python) is advised.

3.

We need to trace the calls between different services.

First we need to find a line where buddy's /run returns with an error:

cat megmerettetes.log | grep buddy] | grep "response status:" | grep -v "response status: 200"
This is the first line of the result:

2024-09-27 12:24:12.467 DEBUG   --- [          buddy] [cfbcbcba-684f-4159-bb96-626a954d6b24] [4c7fa903-c56b-4431-848b-d902c5c4bd49] /run : response status: 400
Now we have a trace ID. With that, we can investigate which services took part in that call chain. We also want to sort the output so it'll be easier to analyze:

cat megmerettetes.log | grep -F "[cfbcbcba-684f-4159-bb96-626a954d6b24]" | grep "response status:" | sort
We get the following output:

2024-09-27 12:24:12.442 DEBUG   --- [           fido] [cfbcbcba-684f-4159-bb96-626a954d6b24] [d978a208-e662-407a-ad96-1c2097300dfe] /run : response status: 400
2024-09-27 12:24:12.451 DEBUG   --- [         sootie] [cfbcbcba-684f-4159-bb96-626a954d6b24] [69904558-35ad-4052-b99c-13fec18cfd05] /run : response status: 400
2024-09-27 12:24:12.458 DEBUG   --- [          furby] [cfbcbcba-684f-4159-bb96-626a954d6b24] [75cb2b8f-4d02-4295-87c8-cfe9e3ab8389] /run : response status: 400
2024-09-27 12:24:12.461 DEBUG   --- [          bingo] [cfbcbcba-684f-4159-bb96-626a954d6b24] [017ad791-881f-4e7c-ab20-e855813bec15] /run : response status: 400
2024-09-27 12:24:12.463 DEBUG   --- [       princess] [cfbcbcba-684f-4159-bb96-626a954d6b24] [31870d0c-b2f7-4488-8098-b59491ee3c28] /run : response status: 400
2024-09-27 12:24:12.467 DEBUG   --- [          buddy] [cfbcbcba-684f-4159-bb96-626a954d6b24] [4c7fa903-c56b-4431-848b-d902c5c4bd49] /run : response status: 400
We are looking for the first service that doesn't return with HTTP OK, which is fido.

To double-check, we can repeat the process with more trace IDs; the result will be the same.