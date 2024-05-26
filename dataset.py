import torch
from torch.utils.data import Dataset

class Shakespeare(Dataset):
    """
    Shakespeare dataset
    To write custom datasets, refer to https://pytorch.org/tutorials/beginner/data_loading_tutorial.html

    Args:
        input_file: txt file

    Note:
        1) Load input file and construct character dictionary {index:character}.
           You need this dictionary to generate characters.
        2) Make list of character indices using the dictionary
        3) Split the data into chunks of sequence length 30. You should create targets appropriately.
    """
    def __init__(self, input_file):
        with open(input_file, 'r') as file:
            self.text = file.read()

        # Create character dictionary
        self.chars = sorted(list(set(self.text)))
        self.char_to_idx = {char: idx for idx, char in enumerate(self.chars)}
        self.idx_to_char = {idx: char for idx, char in enumerate(self.chars)}

        # Convert all characters in the text to indices
        self.data = [self.char_to_idx[char] for char in self.text]

        # Define the sequence length
        self.seq_length = 30
        self.data_len = len(self.data) - self.seq_length

    def __len__(self):
        return self.data_len

    def __getitem__(self, idx):
        input_seq = self.data[idx:idx + self.seq_length]
        target_seq = self.data[idx + 1:idx + self.seq_length + 1]
        return torch.tensor(input_seq), torch.tensor(target_seq)

if __name__ == '__main__':
    dataset = Shakespeare(input_file='shakespeare_train.txt')
    print(f'Dataset length: {len(dataset)}')
    print('Sample data (input, target):')
    for i in range(3):
        input_seq, target_seq = dataset[i]
        print(f'Input: {input_seq}')
        print(f'Target: {target_seq}')
