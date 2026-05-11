import torch
import torch.nn as nn
from torchvision import models
import os

def load_orientation_classifier(device):
    """
    Loads the pre-trained ResNet18 model for spatial orientation detection.
    """
    orientation_classes = ['axial', 'coronal', 'sagitall']
    
    # Initialize base ResNet
    model_orient = models.resnet18(weights=None)
    model_orient.fc = nn.Linear(model_orient.fc.in_features, len(orientation_classes))
    
    # Load proprietary weights securely
    weights_path = os.path.join('saved_models', 'resnet18_router.pth')
    
    if os.path.exists(weights_path):
        model_orient.load_state_dict(torch.load(weights_path, map_location=device, weights_only=True))
    
    model_orient = model_orient.to(device)
    model_orient.eval()
    
    return model_orient, orientation_classes
