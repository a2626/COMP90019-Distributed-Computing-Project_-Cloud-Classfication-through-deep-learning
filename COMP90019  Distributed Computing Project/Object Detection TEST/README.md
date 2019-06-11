# Required library
* TensorFlow Object Detection

# Install
* Can be found at https://github.com/tensorflow/models/tree/master/research/object_detection

# Useful commands
1. <code>From tensorflow/models/research/
 export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim</code>
 
2. <code>python train.py --logtostderr --train_dir=TRAINING_PATH --pipeline_config_path= CONFIG_PATH </code>
	
3. <code>tensorboard --logdir= TEST_MODEL_PATH</code>	
4. <code>python eval.py --logtostderr --pipeline_config_path= CONFIGURATION_PATH  --checkpoint_dir= CHECKPOINT_PATH --eval_dir= RESULT_PATH </code>
5. <code>python export_inference_graph.py --input_type=image_tensor  --pipeline_config_path= CONFIG_PATH  --trained_checkpoint_prefix= TRAINING_PATH  --output_directory= RESULT_PATH </code>
  

