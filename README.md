# Language-Modeling
- a neural network for character-level language modeling.
-----------------------------------------------------------------------------
### Dataset
* Shakespeare
------------------------------------------------------------------------------
### Comparing Loss
#### Training Loss
![training_loss_plot](https://github.com/Day-bi/Language-Modeling/assets/73453720/ca514d71-1aed-4652-9f02-208152b18af8)
- **RNN**: Starts with an initial loss of 1.6 and gradually decreases, converging to around 1.3 at epoch 20
- **LSTM**: Starts with an initial loss of 1.7 and decreases rapidly, converging to around 0.9 at epoch 20. Shows a faster and lower loss compared to RNN
#### Validation Loss
![validation_loss_plot](https://github.com/Day-bi/Language-Modeling/assets/73453720/6d693365-077a-4802-a6d3-00016bce593b)
- **RNN**: Starts with an initial loss of 1.4 and gradually decreases, converging to around 1.3 at epoch 20
- **LSTM**: Starts with an initial loss of 1.4 and decreases rapidly, converging to around 0.9 at epoch 20. Demonstrates better performance compared to RNN

#### Conclusion
- **LSTM's Superiority**: Outperforms RNN in both training and validation loss, reaching lower loss values more quickly
- **RNN's Limitations**: Shows slower reduction in loss and plateaus after certain epochs, indicating limitations in learning complex patterns
- **LSTM Strengths**: Convergence to a lower loss, making it more effective in learning complex sequences
------------------------------------------------------------------------------
### Comparing generated text
* T = 1
  * RNN
      * QUEEN ELIZABETH:zecreed, siring in their general intering the chargine are what our voices. The gods long, as he las
  * LSTM
      * zarent That more to good clute. First Murderer:
      Why, this such a coverture Rome,
      Or bitterly to thy
* T = 10
  * RNN
      * QUEEN ELIZABETH:zin,'d!VCw;
Q-y
VSnUSurwW
Gtb!lwcRjGgcumnw'tapisevn'smk kGxKr!-Watr'ti-g;!UVywyA,YviWvIdj;x evcoOGrS

  * LSTM
      * QUEEN ELIZABETH:z
ipWleaFlyin, ALYuoj. b;d'Neek.
S;il
k'NaMq
bHCafitgpi.
iPboys, Divinct,hPe-Saa-tDbsKEumugh.
O fgBo
