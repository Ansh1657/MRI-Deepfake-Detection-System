from torchvision import transforms
from PIL import Image

# Standard vision transform for the classification models
vision_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Helper for PIL Image conversion from GAN output
to_pil = transforms.ToPILImage()

def rotate_image(img):
    """Rotates the uploaded MRI scan 90 degrees clockwise for standardization."""
    if img is None: 
        return None
    return img.transpose(Image.ROTATE_270)
