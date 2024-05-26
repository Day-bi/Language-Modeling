import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import torch
import torch.optim as optim
import torch.nn as nn
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, random_split

from dataset import Shakespeare
from model import CharRNN, CharLSTM

def train(model, dataloader, device, criterion, optimizer, is_lstm):
    model.train()
    total_loss = 0
    for inputs, targets in dataloader:
        inputs, targets = inputs.to(device), targets.to(device)
        hidden = model.init_hidden(inputs.size(0))
        if is_lstm:
            hidden = (hidden[0].to(device), hidden[1].to(device))
        else:
            hidden = hidden.to(device)
        optimizer.zero_grad()
        output, hidden = model(inputs, hidden)
        loss = criterion(output.view(-1, model.output_size), targets.view(-1))
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(dataloader)

def validate(model, dataloader, device, criterion, is_lstm):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for inputs, targets in dataloader:
            inputs, targets = inputs.to(device), targets.to(device)
            hidden = model.init_hidden(inputs.size(0))
            if is_lstm:
                hidden = (hidden[0].to(device), hidden[1].to(device))
            else:
                hidden = hidden.to(device)
            output, hidden = model(inputs, hidden)
            loss = criterion(output.view(-1, model.output_size), targets.view(-1))
            total_loss += loss.item()
    return total_loss / len(dataloader)

def run_training(model_class, model_name, dataset, train_loader, val_loader, device, hidden_size, n_layers, learning_rate, num_epochs, is_lstm):
    model = model_class(input_size=len(dataset.chars), hidden_size=hidden_size, output_size=len(dataset.chars), n_layers=n_layers).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    train_losses = []
    val_losses = []
    for epoch in range(num_epochs):
        train_loss = train(model, train_loader, device, criterion, optimizer, is_lstm)
        val_loss = validate(model, val_loader, device, criterion, is_lstm)

        train_losses.append(train_loss)
        val_losses.append(val_loss)

        print(f'{model_name} Epoch [{epoch+1}/{num_epochs}], Train Loss: {train_loss:.4f}, Validation Loss: {val_loss:.4f}')

    torch.save(model.state_dict(), f'{model_name}_model.pth')
    
    return train_losses, val_losses

def main():
    # Parameters
    input_file = 'shakespeare_train.txt'
    batch_size = 64
    seq_length = 30
    hidden_size = 128
    n_layers = 2
    learning_rate = 0.002
    num_epochs = 20
    split_ratio = 0.8

    # Device configuration
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load dataset
    dataset = Shakespeare(input_file)
    dataset_size = len(dataset)
    train_size = int(split_ratio * dataset_size)
    val_size = dataset_size - train_size

    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    # Train RNN model
    rnn_train_losses, rnn_val_losses = run_training(
        CharRNN, 'RNN', dataset, train_loader, val_loader, device, hidden_size, n_layers, learning_rate, num_epochs, is_lstm=False
    )

    # Train LSTM model
    lstm_train_losses, lstm_val_losses = run_training(
        CharLSTM, 'LSTM', dataset, train_loader, val_loader, device, hidden_size, n_layers, learning_rate, num_epochs, is_lstm=True
    )

    # Plot the training loss for both models
    plt.figure()
    plt.plot(rnn_train_losses, label='RNN Train Loss')
    plt.plot(lstm_train_losses, label='LSTM Train Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Training Loss')
    plt.savefig('training_loss_plot.png')  # Save the plot as a file
    plt.show()

    # Plot the validation loss for both models
    plt.figure()
    plt.plot(rnn_val_losses, label='RNN Validation Loss')
    plt.plot(lstm_val_losses, label='LSTM Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Validation Loss')
    plt.savefig('validation_loss_plot.png')  # Save the plot as a file
    plt.show()

if __name__ == '__main__':
    main()
