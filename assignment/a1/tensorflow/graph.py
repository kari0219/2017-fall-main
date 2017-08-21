import numpy as np
import tensorflow as tf

class AddTwo(object):
    def __init__(self):
        '''Construct a graph to add two numbers.

        If you are constructing more than one graph within a Python kernel
        you can either tf.reset_default_graph() each time, or you can
        instantiate a tf.Graph() object and construct the graph within it.

        Hint: Recall from live sessions that TensorFlow
        splits its models into two chunks of code:
        - construct and keep around a graph of ops
        - execute ops in the graph
        
        Construct your graph in __init__ and run the ops in Add.
        
        We make the separation explicit in this first subpart to
        drive the point home.  Usually you will just do them all
        in one place, including throughout the rest of this assignment.
        
        Hint:  You'll want to look at tf.placeholder
        Hint:  Look at tf.add(op1, op2).
        Hint:  "op1 + op2" is syntactic sugar so you can write it that way too!
        Hint:  Only write one line of code per instruction/comment below.
        '''

        # START YOUR CODE
        self.graph = tf.Graph()
        with self.graph.as_default():
            self.sess = tf.Session()
            # Create a placeholder op for the first number to add.
            # Store a reference to it in self.x

            # Create a placeholder for the second number to add.
            # Store a reference to it in self.y

            # Create an op to add the two placeholders. Store it in self.z
        # END YOUR CODE

    def Add(self, x, y):
        '''Compute x + y using the graph constructed above.
        Args:
          x: The first value to add.
          y: The second value to add.

        Returns: The sum, x + y

        Hint: look at session.run(...) API.
        '''

        # "pass" is a no-op.  It's here to give the function a body so that
        # this file parses as valid python while you work on other sections.
        pass
              
        # START YOUR CODE
        # Execute the graph you constructed in __init__ using the actual
        # numbers provided in "x" and "y".
        # END YOUR CODE

def affine_layer(hidden_dim, x, seed=0):
    '''Create an affine transformation.

    An affine transformation from linear algebra is "xW + b".

    Note that we want to compute this affine function on each
    feature vector "x" in a batch of examples and return the corresponding
    transformed vectors, each of dimension "hidden_dim".

    Args:
      x: an op representing the features/incoming layer.
         The tensor that this op provides is of shape [batch_size x #features].
         (recall batch_size is the # of examples we want to predict in parallel)
      hidden_dim: a scalar defining the dimension of each output vector.
      seed: use this seed for Xavier initialization.

    Returns: a tensorflow op, when evaluated returns a tensor of dimension
             [batch_size x hidden_dim].

    Hint: On scrap paper, drop a picture of the matrix math xW + b.
    Hint: When doing the previous, make sure you draw "x" as [batch size x features]
          and the shape of the desired output as [batch_size x hidden_dim].
    Hint: use tf.get_variable to create trainable variables.
    Hint: use xavier initialization to initialize "W"
    Hint: always initialize "b" as 0s.  It isn't a constant though!
          It needs to be a trainable variable!
    '''
    pass

    # START YOUR CODE

    # Draw the sketch suggested in the hint above.
    # Include a photo of the sketch in your submission.
    # In your sketch, label all matrix/vector dimensions.

    # Create trainable variables "W" and "b"

    # Return xW + b.
    # END YOUR CODE

def fully_connected_layers(hidden_dims, x):
    '''Construct fully connected layer(s).

    You want to construct:

    x ---> [ xW + b -> relu(.) ]* ---> output

    where the middle block is repeated 0 or more times, determined
    by the len(hidden_dims).

    Args:
      hidden_dims: A list of the width(s) of the hidden layer.
      x: a TensorFlow "op" that will evaluate to a tensor of dimension [batch_size x input_dim].

    To get the tests to pass, you must use tf.nn.relu(.) as your element-wise nonlinearity.
    
    Hint: see tf.variable_scope - you'll want to use this to make each layer 
    unique.

    Hint: a fully connected layer is a nonlinearity of an affine of its input.
          your answer here only be a couple of lines long (mine is 4).

    Hint: use your affine_layer(.) function above to construct the affine part
          of this graph.

    Hint: if hidden_dims is empty, just return x.
    
    Hint: Look at tf.identity(.)
    '''

    # START YOUR CODE
    pass
    # END YOUR CODE

def train_nn(X, y, X_test, hidden_dims, batch_size, num_epochs, learning_rate,
             verbose=False):
    '''
    Train a neural network consisting of fully_connected_layers.

    Use sigmoid_cross_entropy_with_logits loss between the prediction and the
    label, y.

    Args:
      X: train features [batch_size x features]
      Y: train labels [batch_size]
      X_test: test features [test_batch_size x features]
      hidden_dims: same as in fully_connected_layers
      learning_rate: the learning rate for your GradientDescentOptimizer.

    Returns: the predicted y label for X_test.

    Hint: your final graph should look like this:

    x ->  [Fully Connected Layer]* -> Affine Layer (scalar output, called "logits") -> Sigmoid -> y
                                                                                    |-> Loss(., y)

    Hint: Verify the dimensions of each of your variables as you work using .get_shape().
    Hint: Gracefully handle the case of no fully connected layers.
    Hint: The final affine layer is there to change the final output dimension
          to a scalar regardless of what the fully connected layer does.
    Hint: the nonlinearity associated with the final affine layer is the sigmoid
          (sometimes the "softmax" in other problems we'll see layer in the course).
          Specifically, you should not do Affine->Relu->Sigmoid.  Just Affine->Sigmoid.
    Hint: See more hints below in comments around the code you are to write!
    '''

    # Construct the placeholders.
    tf.reset_default_graph()
    x_ph = tf.placeholder(tf.float32, shape=[None, X.shape[-1]])
    y_ph = tf.placeholder(tf.float32, shape=[None])
    global_step = tf.Variable(0, trainable=False)

    # Construct the neural network, store the batch loss in a variable called `loss`.
    # At the end of this block, you'll want to have these ops:
    # - y_hat: probability of the positive class
    # - loss: the average cross entropy loss across the batch
    #   (hint: see tf.sigmoid_cross_entropy_with_logits)
    #   (hint 2: see tf.reduce_mean to go from a per-item loss to a batch-wide loss)
    # - train_op: the training operation resulting from minimizing the loss
    #             with a GradientDescentOptimizer
    # - dimensions: you'll want to wrap the output of your final affine layer with
    #               tf.squeeze.  Make sure you specify the squeeze_dims parameter!
    #
    # START YOUR CODE

    # END YOUR CODE


    # Output some initial statistics.
    sess = tf.Session(config=tf.ConfigProto(device_filters="/cpu:0"))
    # sess.run(tf.initialize_all_variables())
    sess.run(tf.global_variables_initializer())
    print 'Initial loss:', sess.run(loss, feed_dict={x_ph: X, y_ph: y})

    if verbose:
      for var in tf.trainable_variables():
          print 'Variable: ', var.name, var.get_shape()
          print 'dJ/dVar: ', sess.run(
                  tf.gradients(loss, var), feed_dict={x_ph: X, y_ph: y})

    for epoch_num in xrange(num_epochs):
        for batch in xrange(0, X.shape[0], batch_size):
            X_batch = X[batch : batch + batch_size]
            y_batch = y[batch : batch + batch_size]

            # Feed a batch to your network using sess.run.
            # Hint: Evaluate the global_step variable you created above.
            # Hint: You'll also want to run your training op and loss.
            # Hint: Evaluate all three in a single call to session.run.
            # Hint: To be clear, do not call session.run more than once!
            # START YOUR CODE
            global_step_value, loss_value, train_op_value = (
                    )
            # END YOUR CODE
        if epoch_num % 300 == 0:
            print 'Step: ', global_step_value, 'Loss:', loss_value
            if verbose:
              for var in tf.trainable_variables():
                  print var.name, sess.run(var)
              print ''

    # Return your predictions.
    #
    # Hint: Evaluating the y_hat node in the graph here will return the probability of
    #       the positive class, not the class label.  But the function requires that
    #       you return the class label.
    #       You can either add more to your graph to output the class label and evaluate
    #       that instead.  Or, more easily, you can just sess.run(y_hat, ...) here
    #       which will give you a NumPy array back that you can work with directly
    #       outside of TF to threshold at 0.5.
    #
    # Hint: Make sure you evaluate X_test, not X_train!

    # START YOUR CODE
    # END YOUR CODE
