# Covid_Detecion
In this program, we read a dataset of x-ray images that includes classes: Normal, Covid and Viral, and then we categorize the data using the resnet18 network.
Here we only train the last layer of the resnet18 network and in other words we train the network using the transfer learning method.

## Block Diagram CnnTransformer
![block_diagram_cnntransformer3](https://github.com/SayedMahdiMousavi/Covid_Detecion/assets/56066734/8bc8e724-24b4-47ba-a886-5a8964a10851)


## Results

### Accuracy
|                           |     Train    |     Validation    |     Test    |
|---------------------------|--------------|-------------------|-------------|
|     CnnTransformer        |     0.95     |     0.93          |     0.92    |
|     Cnn                   |     0.92     |     0.91          |     0.89    |
|     EffiecientNet_V2_S    |     0.99     |     0.96          |     0.95    |
|     Swin Transformer      |     0.97     |     0.95          |     0.95    |


### Loss
|                           |     Train    |     Validation    |     Test    |
|---------------------------|--------------|-------------------|-------------|
|     CnnTransformer        |     0.14     |     0.19          |     0.23    |
|     Cnn                   |     0.24     |     0.25          |     0.3     |
|     EffiecientNet_V2_S    |     0.05     |     0.14          |     0.17    |
|     Swin Transformer      |     0.9      |     0.15          |     0.17    |

## number of parameters
|               |     CnnTransformer    |     Cnn          |     EffiecientNet    |     Swin Transformer    |
|---------------|-----------------------|------------------|----------------------|-------------------------|
|     Params    |     11,276,804        |     1,554,948    |     20,182,612       |     27,522,430          |
