import torch


torchBackendMps = hasattr(torch.backends, "mps")
torchBackendIsAvailable = torch.backends.mps.is_available()

print("torchBackendMps: " + str(torchBackendMps) + " torchBackendIsAvailable: " + str(torchBackendIsAvailable))

