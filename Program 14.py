import tensorflow as tf
rnn = tf.keras.Sequential([
    tf.keras.layers.SimpleRNN(units=32, input_shape=(None, 1)),
    tf.keras.layers.Dense(units=1)
])
rnn.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam())
X = [[i] for i in range(20)]
y = [i[0] + 5 for i in X]
X = tf.reshape(tf.convert_to_tensor(X, dtype=tf.float32), [-1, 1, 1])
y = tf.reshape(tf.convert_to_tensor(y, dtype=tf.float32), [-1, 1])
rnn.fit(X, y, epochs=50)
test_X = [[i] for i in range(20, 30)]
test_X = tf.reshape(tf.convert_to_tensor(test_X, dtype=tf.float32), [-1, 1, 1])
predictions = rnn.predict(test_X)
print(predictions)
