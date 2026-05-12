import torch
import os
from PIL import Image
from src.models.dcgan import Generator
from src.preprocessing.standardize import to_pil

def synthesize_mri(contrast_label, device):
    """
    Dynamically loads the correct GAN architecture based on the sequence 
    (Bright/Dark) and synthesizes a deepfake twin from latent noise.
    """
    # Route to Local GAN
    gan_weights_path = os.path.join('saved_models', 'dcgan_bright.pth') if "Bright" in contrast_label else os.path.join('saved_models', 'dcgan_dark.pth')

    if not os.path.exists(gan_weights_path):
        return None, f"\n⚠️ Warning: Could not find GAN weights at {gan_weights_path}"

    # Initialize and load weights
    netG = Generator().to(device)
    netG.load_state_dict(torch.load(gan_weights_path, map_location=device, weights_only=True))
    netG.eval()

    # Generate synthetic image
    with torch.no_grad():
        noise = torch.randn(1, 100, 1, 1, device=device)
        fake_tensor = netG(noise)
        fake_tensor = (fake_tensor.squeeze(0) + 1) / 2.0
        
        # Convert tensor back to image format
        synthetic_twin_img = to_pil(fake_tensor.cpu())
        synthetic_twin_img = synthetic_twin_img.resize((256, 256), Image.Resampling.NEAREST)

    # Clean up memory
    del netG
    
    return synthetic_twin_img, ""
