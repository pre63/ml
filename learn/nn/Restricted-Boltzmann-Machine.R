# install CRAN packages
# options(repos = c(CRAN = "https://cran.rstudio.com/"))
# install.packages("dplyr")

library(dplyr)

# Initialize weights and biases
initialize_parameters <- function(num_visible, num_hidden) {
  list(weights = matrix(rnorm(num_visible * num_hidden, mean = 0, sd = 0.1), nrow = num_visible, ncol = num_hidden),
       visible_bias = rep(0, num_visible),
       hidden_bias = rep(0, num_hidden))
}


# Activation probability function
activation_probability <- function(weights, bias, data) {
  1 / (1 + exp(-(data %*% weights + bias)))
}

# Gibbs sampling step
gibbs_sample <- function(data, params) {
  # Positive phase
  pos_hidden_probs = activation_probability(params$weights, params$hidden_bias, data)
  pos_hidden_states = ifelse(runif(length(pos_hidden_probs)) < pos_hidden_probs, 1, 0)
  
  # Negative phase
  neg_visible_probs = activation_probability(t(params$weights), params$visible_bias, pos_hidden_states)
  neg_visible_states = ifelse(runif(length(neg_visible_probs)) < neg_visible_probs, 1, 0)
  neg_hidden_probs = activation_probability(params$weights, params$hidden_bias, neg_visible_states)
  
  list(pos_hidden_probs = pos_hidden_probs,
       neg_visible_probs = neg_visible_probs,
       neg_hidden_probs = neg_hidden_probs,
       pos_hidden_states = pos_hidden_states,
       neg_visible_states = neg_visible_states)
}

train_rbm <- function(data, num_hidden, num_epochs, learning_rate) {
  num_visible = ncol(data)
  params = initialize_parameters(num_visible, num_hidden)
  
  for(epoch in 1:num_epochs) {
    for(i in 1:nrow(data)) {
      sample = gibbs_sample(data[i, , drop = FALSE], params)
      
      # Update rules for weights and biases
      data_i = matrix(data[i, ], nrow = 1)
      weight_update = learning_rate * ((t(data_i) %*% sample$pos_hidden_probs) - (t(sample$neg_visible_states) %*% sample$neg_hidden_probs))
      visible_bias_update = learning_rate * (data_i - sample$neg_visible_states)
      hidden_bias_update = learning_rate * (sample$pos_hidden_probs - sample$neg_hidden_probs)
      
      params$weights = params$weights + weight_update
      params$visible_bias = params$visible_bias + t(visible_bias_update)
      params$hidden_bias = params$hidden_bias + t(hidden_bias_update)
    }
  }
  params
}

# Dummy binary data matrix
set.seed(123)
data_matrix = matrix(rbinom(100, 1, 0.5), ncol = 10)

# Training RBM
rbm_params = train_rbm(data_matrix, num_hidden = 5, num_epochs = 1000, learning_rate = 0.01)


image(rbm_params$weights, main = "Weights of the RBM")
