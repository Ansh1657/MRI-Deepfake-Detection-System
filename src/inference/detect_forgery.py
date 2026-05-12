import torch

def analyze_scan(img_tensor, model_detect, model_orient, orientation_classes):
    """
    Executes the forward pass for both the ResNet orientation router 
    and the Custom CNN Deepfake Detector.
    """
    with torch.no_grad():
        # 1. Orientation Classification
        orient_out = model_orient(img_tensor)
        orient_idx = torch.argmax(orient_out, 1).item()
        plane_label = orientation_classes[orient_idx]

        # 2. Deepfake Detection (BCEWithLogits uses Sigmoid)
        detect_out = model_detect(img_tensor)
        prob_fake = torch.sigmoid(detect_out).item()

    # Format the confidence scores
    verdict_dict = {"FAKE": prob_fake, "REAL": 1.0 - prob_fake}
    
    return verdict_dict, plane_label
