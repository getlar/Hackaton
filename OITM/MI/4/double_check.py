import tensorflow as tf

input_tensor = tf.keras.layers.Input(shape=(60, 40, 3))
conv_layer = tf.keras.layers.Conv2D(1, (5, 5), padding='valid', activation='relu')(input_tensor)
max_pooling_layer = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid')(conv_layer)
model = tf.keras.Model(inputs=input_tensor, outputs=max_pooling_layer)
model.summary()