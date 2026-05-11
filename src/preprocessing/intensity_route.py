import numpy as np

def determine_sequence_type(img):
    """
    Analyzes the grayscale intensity of the MRI to route it to the 
    appropriate downstream GAN (T1_Dark vs FLAIR_Bright).
    """
    img_cv = np.array(img.convert('L'))
    
    # Mask out the pure black background
    mask = img_cv > 10
    mean_intensity = np.mean(img_cv[mask]) if np.any(mask) else 0
    
    # Threshold routing logic
    contrast_label = "T1_Dark" if mean_intensity < 65 else "FLAIR_Bright"
    
    return contrast_label, mean_intensity
