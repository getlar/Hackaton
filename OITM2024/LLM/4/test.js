// Step 1: Build the initial sequence
function buildSequence(n, factor) {
    let sequence = [];
    for (let i = 0; i < n; i++) {
        let value = (i * factor) % 26; // Generate values modulo 26
        sequence.push(value);
    }
    return sequence;
}

// Step 2: Adjust the sequence with modifiers
function adjustSequence(seq, modifier1, modifier2) {
    let adjusted = [];
    for (let i = 0; i < seq.length; i++) {
        let newValue;
        if (i % 2 === 0) {
            newValue = (seq[i] + modifier1) % 26; // Apply modifier1 for even indices
        } else {
            newValue = (seq[i] - modifier2 + 26) % 26; // Apply modifier2 for odd indices, ensuring non-negative
        }
        adjusted.push(newValue);
    }
    return adjusted;
}

// Step 3: Merge two sequences together
function mergeSequences(seq1, seq2) {
    let merged = [];
    for (let i = 0; i < seq1.length; i++) {
        let mergedValue = (seq1[i] + seq2[i]) % 26; // Add values and apply modulo 26
        merged.push(mergedValue);
    }
    return merged;
}

// Step 4: Generate an output string from the sequence
function generateOutputString(seq) {
    let output = '';
    for (let i = 0; i < seq.length; i++) {
        let char = String.fromCharCode(97 + seq[i]); // Map 0-25 to 'a'-'z'
        output += char;
    }
    return output;
}

// Step 5: Combine the sequence generation process
function complexProcess(n, factor, mod1, mod2) {
    let seq1 = buildSequence(n, factor); // Step 1
    let seq2 = adjustSequence(seq1, mod1, mod2); // Step 2
    let mergedSeq = mergeSequences(seq1, seq2); // Step 3
    return mergedSeq; // Return the final merged sequence as numbers
}

// Step 6: Execute the process for multiple iterations and create a single sequence
function finalComputation(n, factor, mod1, mod2, iterations) {
    let combinedSequence = [];
    for (let i = 0; i < iterations; i++) {
        let iterationResult = complexProcess(n, factor, mod1, mod2); // Perform one iteration
        combinedSequence = combinedSequence.concat(iterationResult); // Combine sequences across iterations
    }
    return generateOutputString(combinedSequence); // Convert the combined sequence into a string
}

// Main execution function
function mainExecution() {
    let n = 5;
    let factor = 3;
    let mod1 = 7;
    let mod2 = 2;
    let iterations = 4;

    let result = finalComputation(n, factor, mod1, mod2, iterations);
    console.log("Final Encoded Word:", result);
}
mainExecution();
