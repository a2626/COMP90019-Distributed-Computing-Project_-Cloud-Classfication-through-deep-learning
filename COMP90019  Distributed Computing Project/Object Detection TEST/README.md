# Required library
* TensorFlow Object Detection

# Install
* Can be found at https://github.com/tensorflow/models/tree/master/research/object_detection

# Useful command
* <code>From tensorflow/models/research/
 export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim</code>
 
* <code>python train.py --logtostderr --train_dir=TRAINING_PATH --pipeline_config_path= CONFIG_PATH </code>
  Training the model
	
* <code>tensorboard --logdir= TEST_MODEL_PATH</code>	
* <code>python eval.py --logtostderr --pipeline_config_path= CONFIGURATION_PATH  --checkpoint_dir= CHECKPOINT_PATH --eval_dir= RESULT_PATH </code>
* <code>python export_inference_graph.py --input_type=image_tensor  --pipeline_config_path= CONFIG_PATH  --trained_checkpoint_prefix= TRAINING_PATH  --output_directory= RESULT_PATH </code>
  

