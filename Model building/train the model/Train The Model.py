model.fit_generator(x_train,steps_per_epoch = len(x_train),epochs=25,validation_data=x_test,validation_steps = len(x_test))