
import torch
from torchvision import models
from torch import nn


torch.manual_seed(0)

model = models.vgg19(pretrained=True)
model.train = False
new_classifier =  model.classifier[:-3]
model.classifier = new_classifier
print(model)
torch.save(model, 'model.pt')











