x_train=train_datagen.flow_from_directory( 'C:\Dataset\train',target_size=(64,64),batch_size=5,color_mode='grayscale',class_mode='categorical')
x_test=test_datagen.flow_from_directory( 'C:\Dataset\test',target_size=(64,64),batch_size=5,color_mode='grayscale',class_mode='categorical')
