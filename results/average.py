from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2
import os

def mse(imageA, imageB):
    # Calculate the Mean Squared Error between two images
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def run_average(orig_image_directory, corrected_image_directory, num_images):
    # Write down the path to directory containing images
    # orig_image_directory = "../laboro_tomato/test_downsized"
    # corrected_image_directory = f"cnn_results/training_results_{intensity}"
    # num_images = 150  # However many images there are - I just assumed 1500

    total_mse = 0
    total_ssim = 0

    for i in range(num_images):
        original_path = os.path.join(orig_image_directory, f"original_{i}.png")
        corrected_path = os.path.join(corrected_image_directory, f"sim_corrected_{i}.png") #I based this off of Satyam's images, hopefully everyone else is using the same template. If not, change as you want. 

        # Load the images
        original = cv2.imread(original_path)
        corrected = cv2.imread(corrected_path)

        # Calculate SSIM and MSE for the current pair
        
        m = mse(original, corrected)
        s = ssim(original, corrected, channel_axis=2)

        print(f"Pair {i}: Avg MSE: {m:.2f}, Avg SSIM: {s:.2f}")

        total_mse += m
        total_ssim += s

    # Calculate the average MSE and SSIM across all pairs
    avg_mse_total = total_mse / (num_images + 1)
    avg_ssim_total = total_ssim / (num_images + 1)

    print(f"Average MSE across all pairs: {avg_mse_total:.2f}")
    print(f"Average SSIM across all pairs: {avg_ssim_total:.2f}")
    return avg_mse_total, avg_ssim_total