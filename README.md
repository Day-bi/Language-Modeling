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
  ![image](https://github.com/Day-bi/Language-Modeling/assets/73453720/c7e7736f-80d3-4bc1-a62a-161360a530f3)



  * LSTM
      * zarent That more to good clute. First Murderer:
      Why, this such a coverture Rome,
      Or bitterly to thy
    ![image](https://github.com/Day-bi/Language-Modeling/assets/73453720/bfb31a33-88f5-4d22-9835-20805e2eebb5)


* T = 10
  * RNN
      * QUEEN ELIZABETH:zin,'d!VCw;Q-yVSnUSurwWGtb!lwcRjGgcumnw'tapisevn'smk kGxKr!-Watr'ti-g;!UVywyA,YviWvIdj;x evcoOGrS
    ![image](https://github.com/Day-bi/Language-Modeling/assets/73453720/5b6fb182-a8f1-4dc7-b348-c4d93b80b0cd)

  * LSTM
      * QUEEN ELIZABETH:zipWleaFlyin, ALYuoj. b;d'Neek.S;ilk'NaMqbHCafitgpi.iPboys, Divinct,hPe-Saa-tDbsKEumugh.O fgBo
    ![image](https://github.com/Day-bi/Language-Modeling/assets/73453720/81e0c6f6-b25d-4d75-bef0-5981eec40b62)
