import torch
from torch_geometric.data import Data


print(torch.__version__)
print(torch.cuda.is_available())

edge_index = torch.tensor([[0, 1, 1, 2],
                           [1, 0, 2, 1]], dtype=torch.long)
x = torch.tensor([[-1], [0], [1]], dtype=torch.float)
data = Data(x=x, edge_index=edge_index)
print(data.keys)

