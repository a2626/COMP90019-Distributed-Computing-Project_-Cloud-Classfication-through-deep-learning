# Required library
* TensorFlow Object Detection

# Install
* Can be found at https://github.com/tensorflow/models/tree/master/research/object_detection

# Useful command

* From tensorflow/models/research/
 export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
 <p>Every time when we perform TensorFlow API, we have to use this command to initial the environment. Otherwise, it will showed some error.<p>
* python train.py --logtostderr --train_dir=TRAINING_PATH --pipeline_config_path= CONFIG_PATH<p>
  Training the model
* tensorboard --logdir= TEST_MODEL_PATH<p>
  Using tensorboard to see the result
* python eval.py --logtostderr --pipeline_config_path= CONFIGURATION_PATH  --checkpoint_dir= CHECKPOINT_PATH --eval_dir= RESULT_PATH
  Testing the model
* python export_inference_graph.py --input_type=image_tensor  --pipeline_config_path= CONFIG_PATH  --trained_checkpoint_prefix= TRAINING_PATH  --output_directory= RESULT_PATH <p>
  

