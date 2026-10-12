import torch

w = torch.tensor(0.0, requires_grad=True)

optimizer = torch.optim.SGD([w], lr=0.1)

for epoch in range(100):
    optimizer.zero_grad()
    loss = (w - 2)**2
    loss.backward()
    optimizer.step()

print("w =", w.item())
print("loss =", loss.item())