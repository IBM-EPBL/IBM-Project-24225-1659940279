from keras.preprocessing.image import ImageDataGenerator
train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
x_train=train_datagen.flow_from_directory( 'C:\Dataset\train',target_size=(64,64),batch_size=5,color_mode='grayscale',class_mode='categorical')
x_test=test_datagen.flow_from_directory( 'C:\Dataset\test',target_size=(64,64),batch_size=5,color_mode='grayscale',class_mode='categorical')
