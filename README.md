
# **Code Example** 
Code Example

For the sake of brevity, you should download docker and initialize a theano environment. 
```
$ curl -sSL https://get.docker.com/ | sh

$ sudo docker pull kaixhin/theano

$ sudo docker run -i -t kaixhin/theano /bin/bash
```
You should restart your server if your sudo docker commands cannot execute.
You need to install lasagne and follow the default installation for the bleeding-edge version of lasagne
```
$ pip install -r https://raw.githubusercontent.com/Lasagne/Lasagne/master/requirements.txt

$ pip install https://github.com/Lasagne/Lasagne/archive/master.zip

```
You can then clone this repository here 
```
$ cd home

$ git clone git://github.com/muhdamrullah/residual-sean

$ cd residual-sean

$ python deep_residual_learning_for_cifar10_like_datasets.py

```

... When you execute this command, you are taking data_batch_[1-5] as the training set and the last data_batch_5 as the cross-validation set.

You can then generate a csv for kaggle. Please ensure that you have a CIFAR-like unlabelled data and name it 'unlabelled_batch'. This data can have a generic label of '0' or 'NA'.
```
$ python deep_residual_learning_for_cifar10_like_datasets.py_for_labelling.py 5 <name of model in .npz format>
```
