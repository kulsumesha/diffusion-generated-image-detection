100 Epochs (Before Quantization):

mobilenetv4:
Using device: cuda
Classes: ['ai', 'nature']
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Epoch 1/100 | train_loss=2.0325 train_acc=0.7400 | val_loss=1.7522 val_acc=0.7680
Epoch 2/100 | train_loss=1.0726 train_acc=0.8394 | val_loss=1.0997 val_acc=0.8347
Epoch 3/100 | train_loss=0.6534 train_acc=0.8963 | val_loss=1.1515 val_acc=0.8187
Epoch 4/100 | train_loss=0.5313 train_acc=0.9051 | val_loss=0.9751 val_acc=0.8453
Epoch 5/100 | train_loss=0.4297 train_acc=0.9183 | val_loss=1.1163 val_acc=0.8373
Epoch 6/100 | train_loss=0.2974 train_acc=0.9354 | val_loss=0.7759 val_acc=0.8760
Epoch 7/100 | train_loss=0.2772 train_acc=0.9451 | val_loss=0.9449 val_acc=0.8613
Epoch 8/100 | train_loss=0.2205 train_acc=0.9537 | val_loss=0.7640 val_acc=0.8787
Epoch 9/100 | train_loss=0.1745 train_acc=0.9651 | val_loss=0.6683 val_acc=0.8880
Epoch 10/100 | train_loss=0.2059 train_acc=0.9566 | val_loss=0.7254 val_acc=0.8880
Epoch 11/100 | train_loss=0.1687 train_acc=0.9600 | val_loss=0.5248 val_acc=0.9120
Epoch 12/100 | train_loss=0.1415 train_acc=0.9660 | val_loss=0.7752 val_acc=0.8773
Epoch 13/100 | train_loss=0.1021 train_acc=0.9729 | val_loss=0.5143 val_acc=0.9053
Epoch 14/100 | train_loss=0.1149 train_acc=0.9703 | val_loss=0.6103 val_acc=0.8960
Epoch 15/100 | train_loss=0.0978 train_acc=0.9757 | val_loss=0.4910 val_acc=0.9200
Epoch 16/100 | train_loss=0.0686 train_acc=0.9817 | val_loss=0.6703 val_acc=0.8853
Epoch 17/100 | train_loss=0.0872 train_acc=0.9763 | val_loss=0.4421 val_acc=0.9187
Epoch 18/100 | train_loss=0.0745 train_acc=0.9803 | val_loss=0.4763 val_acc=0.9213
Epoch 19/100 | train_loss=0.0904 train_acc=0.9789 | val_loss=0.3329 val_acc=0.9187
Epoch 20/100 | train_loss=0.0651 train_acc=0.9823 | val_loss=0.3662 val_acc=0.9253
Epoch 21/100 | train_loss=0.0494 train_acc=0.9846 | val_loss=0.4822 val_acc=0.9133
Epoch 22/100 | train_loss=0.0781 train_acc=0.9774 | val_loss=0.2894 val_acc=0.9347
Epoch 23/100 | train_loss=0.0551 train_acc=0.9823 | val_loss=0.4027 val_acc=0.9240
Epoch 24/100 | train_loss=0.0425 train_acc=0.9883 | val_loss=0.3522 val_acc=0.9293
Epoch 25/100 | train_loss=0.0683 train_acc=0.9817 | val_loss=0.3510 val_acc=0.9333
Epoch 26/100 | train_loss=0.0635 train_acc=0.9857 | val_loss=0.3066 val_acc=0.9453
Epoch 27/100 | train_loss=0.0507 train_acc=0.9837 | val_loss=0.4240 val_acc=0.9173
Epoch 28/100 | train_loss=0.0429 train_acc=0.9877 | val_loss=0.2337 val_acc=0.9480
Epoch 29/100 | train_loss=0.0459 train_acc=0.9854 | val_loss=0.3396 val_acc=0.9227
Epoch 30/100 | train_loss=0.0533 train_acc=0.9834 | val_loss=0.2873 val_acc=0.9480
Epoch 31/100 | train_loss=0.0584 train_acc=0.9834 | val_loss=0.3161 val_acc=0.9347
Epoch 32/100 | train_loss=0.0904 train_acc=0.9760 | val_loss=0.3375 val_acc=0.9320
Epoch 33/100 | train_loss=0.0458 train_acc=0.9846 | val_loss=0.2378 val_acc=0.9413
Epoch 34/100 | train_loss=0.0303 train_acc=0.9909 | val_loss=0.2476 val_acc=0.9427
Epoch 35/100 | train_loss=0.0300 train_acc=0.9897 | val_loss=0.3258 val_acc=0.9240
Epoch 36/100 | train_loss=0.0197 train_acc=0.9940 | val_loss=0.2308 val_acc=0.9493
Epoch 37/100 | train_loss=0.0422 train_acc=0.9883 | val_loss=0.2795 val_acc=0.9320
Epoch 38/100 | train_loss=0.0516 train_acc=0.9869 | val_loss=0.3361 val_acc=0.9320
Epoch 39/100 | train_loss=0.0309 train_acc=0.9911 | val_loss=0.3140 val_acc=0.9333
Epoch 40/100 | train_loss=0.0321 train_acc=0.9897 | val_loss=0.2737 val_acc=0.9413
Epoch 41/100 | train_loss=0.0246 train_acc=0.9914 | val_loss=0.3496 val_acc=0.9293
Epoch 42/100 | train_loss=0.0418 train_acc=0.9886 | val_loss=0.3506 val_acc=0.9200
Epoch 43/100 | train_loss=0.0423 train_acc=0.9877 | val_loss=0.3388 val_acc=0.9293
Epoch 44/100 | train_loss=0.0154 train_acc=0.9926 | val_loss=0.4683 val_acc=0.9160
Epoch 45/100 | train_loss=0.0433 train_acc=0.9871 | val_loss=0.4092 val_acc=0.9147
Epoch 46/100 | train_loss=0.0373 train_acc=0.9900 | val_loss=0.2898 val_acc=0.9440
Epoch 47/100 | train_loss=0.0138 train_acc=0.9946 | val_loss=0.2168 val_acc=0.9533
Epoch 48/100 | train_loss=0.0210 train_acc=0.9946 | val_loss=0.3013 val_acc=0.9413
Epoch 49/100 | train_loss=0.0853 train_acc=0.9771 | val_loss=0.2225 val_acc=0.9360
Epoch 50/100 | train_loss=0.0475 train_acc=0.9840 | val_loss=0.2481 val_acc=0.9413
Epoch 51/100 | train_loss=0.0366 train_acc=0.9874 | val_loss=0.1994 val_acc=0.9480
Epoch 52/100 | train_loss=0.0432 train_acc=0.9843 | val_loss=0.2848 val_acc=0.9240
Epoch 53/100 | train_loss=0.0233 train_acc=0.9920 | val_loss=0.1714 val_acc=0.9533
Epoch 54/100 | train_loss=0.0180 train_acc=0.9943 | val_loss=0.1771 val_acc=0.9427
Epoch 55/100 | train_loss=0.0180 train_acc=0.9934 | val_loss=0.1554 val_acc=0.9520
Epoch 56/100 | train_loss=0.0137 train_acc=0.9937 | val_loss=0.2123 val_acc=0.9493
Epoch 57/100 | train_loss=0.0311 train_acc=0.9886 | val_loss=0.1734 val_acc=0.9733
Epoch 58/100 | train_loss=0.0239 train_acc=0.9940 | val_loss=0.1969 val_acc=0.9587
Epoch 59/100 | train_loss=0.0113 train_acc=0.9951 | val_loss=0.2032 val_acc=0.9587
Epoch 60/100 | train_loss=0.0348 train_acc=0.9891 | val_loss=0.1924 val_acc=0.9547
Epoch 61/100 | train_loss=0.0252 train_acc=0.9897 | val_loss=0.1486 val_acc=0.9600
Epoch 62/100 | train_loss=0.1374 train_acc=0.9623 | val_loss=0.1355 val_acc=0.9453
Epoch 63/100 | train_loss=0.0369 train_acc=0.9880 | val_loss=0.1820 val_acc=0.9493
Epoch 64/100 | train_loss=0.0267 train_acc=0.9931 | val_loss=0.1486 val_acc=0.9573
Epoch 65/100 | train_loss=0.0186 train_acc=0.9940 | val_loss=0.0989 val_acc=0.9733
Epoch 66/100 | train_loss=0.0372 train_acc=0.9906 | val_loss=0.1563 val_acc=0.9507
Epoch 67/100 | train_loss=0.0834 train_acc=0.9717 | val_loss=0.1571 val_acc=0.9533
Epoch 68/100 | train_loss=0.0175 train_acc=0.9946 | val_loss=0.1616 val_acc=0.9613
Epoch 69/100 | train_loss=0.0339 train_acc=0.9911 | val_loss=0.1781 val_acc=0.9493
Epoch 70/100 | train_loss=0.0136 train_acc=0.9951 | val_loss=0.2242 val_acc=0.9493
Epoch 71/100 | train_loss=0.0180 train_acc=0.9949 | val_loss=0.1951 val_acc=0.9440
Epoch 72/100 | train_loss=0.0213 train_acc=0.9920 | val_loss=0.1447 val_acc=0.9653
Epoch 73/100 | train_loss=0.0229 train_acc=0.9943 | val_loss=0.4229 val_acc=0.9027
Epoch 74/100 | train_loss=0.0134 train_acc=0.9946 | val_loss=0.1277 val_acc=0.9613
Epoch 75/100 | train_loss=0.0278 train_acc=0.9906 | val_loss=0.3196 val_acc=0.9280
Epoch 76/100 | train_loss=0.0190 train_acc=0.9923 | val_loss=0.1953 val_acc=0.9520
Epoch 77/100 | train_loss=0.0431 train_acc=0.9909 | val_loss=0.1478 val_acc=0.9600
Epoch 78/100 | train_loss=0.0232 train_acc=0.9926 | val_loss=0.1482 val_acc=0.9573
Epoch 79/100 | train_loss=0.0232 train_acc=0.9906 | val_loss=0.1730 val_acc=0.9573
Epoch 80/100 | train_loss=0.0991 train_acc=0.9734 | val_loss=0.1928 val_acc=0.9347
Epoch 81/100 | train_loss=0.0431 train_acc=0.9834 | val_loss=0.1531 val_acc=0.9560
Epoch 82/100 | train_loss=0.0153 train_acc=0.9963 | val_loss=0.1432 val_acc=0.9627
Epoch 83/100 | train_loss=0.0164 train_acc=0.9951 | val_loss=0.1687 val_acc=0.9627
Epoch 84/100 | train_loss=0.0238 train_acc=0.9929 | val_loss=0.2385 val_acc=0.9520
Epoch 85/100 | train_loss=0.0090 train_acc=0.9969 | val_loss=0.1366 val_acc=0.9640
Epoch 86/100 | train_loss=0.0147 train_acc=0.9969 | val_loss=0.1973 val_acc=0.9613
Epoch 87/100 | train_loss=0.0121 train_acc=0.9960 | val_loss=0.2159 val_acc=0.9613
Epoch 88/100 | train_loss=0.0215 train_acc=0.9926 | val_loss=0.1891 val_acc=0.9560
Epoch 89/100 | train_loss=0.0344 train_acc=0.9903 | val_loss=0.2060 val_acc=0.9280
Epoch 90/100 | train_loss=0.0203 train_acc=0.9914 | val_loss=0.4581 val_acc=0.9067
Epoch 91/100 | train_loss=0.0139 train_acc=0.9960 | val_loss=0.1466 val_acc=0.9560
Epoch 92/100 | train_loss=0.0219 train_acc=0.9920 | val_loss=0.1810 val_acc=0.9453
Epoch 93/100 | train_loss=0.0096 train_acc=0.9963 | val_loss=0.1686 val_acc=0.9573
Epoch 94/100 | train_loss=0.0158 train_acc=0.9946 | val_loss=0.4738 val_acc=0.9293
Epoch 95/100 | train_loss=0.0100 train_acc=0.9960 | val_loss=0.1280 val_acc=0.9667
Epoch 96/100 | train_loss=0.0136 train_acc=0.9957 | val_loss=0.1025 val_acc=0.9720
Epoch 97/100 | train_loss=0.0046 train_acc=0.9983 | val_loss=0.1757 val_acc=0.9587
Epoch 98/100 | train_loss=0.0019 train_acc=0.9997 | val_loss=0.1123 val_acc=0.9707
Epoch 99/100 | train_loss=0.0237 train_acc=0.9937 | val_loss=0.3085 val_acc=0.9493
Epoch 100/100 | train_loss=0.0637 train_acc=0.9800 | val_loss=0.3862 val_acc=0.9587

Evaluating on test set...
Figure(400x400)
Figure(1200x450)

Done. Results saved to: /content/drive/MyDrive/diffusion_project/results/mobilenetv4/results.json
Checkpoint saved to: /content/drive/MyDrive/diffusion_project/results/mobilenetv4/checkpoint.pth

Summary — mobilenetv4:
  Test Accuracy:  0.9747
  Test Precision: 0.9811
  Test Recall:    0.9680
  Test F1:        0.9745
  Parameters:     2,495,586
  Model size:     9.85 MB
  Avg latency:    0.70 ms/image

efficientnetv2s:
Using device: cuda
Classes: ['ai', 'nature']
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Epoch 1/100 | train_loss=0.6697 train_acc=0.8006 | val_loss=0.2407 val_acc=0.9120
Epoch 2/100 | train_loss=0.1038 train_acc=0.9651 | val_loss=0.1730 val_acc=0.9400
Epoch 3/100 | train_loss=0.0443 train_acc=0.9851 | val_loss=0.1809 val_acc=0.9427
Epoch 4/100 | train_loss=0.0322 train_acc=0.9894 | val_loss=0.2162 val_acc=0.9267
Epoch 5/100 | train_loss=0.0281 train_acc=0.9903 | val_loss=0.1563 val_acc=0.9507
Epoch 6/100 | train_loss=0.0258 train_acc=0.9897 | val_loss=0.1410 val_acc=0.9533
Epoch 7/100 | train_loss=0.0172 train_acc=0.9943 | val_loss=0.1675 val_acc=0.9493
Epoch 8/100 | train_loss=0.0139 train_acc=0.9963 | val_loss=0.1841 val_acc=0.9427
Epoch 9/100 | train_loss=0.0179 train_acc=0.9929 | val_loss=0.1464 val_acc=0.9480
Epoch 10/100 | train_loss=0.0212 train_acc=0.9934 | val_loss=0.1596 val_acc=0.9587
Epoch 11/100 | train_loss=0.0105 train_acc=0.9966 | val_loss=0.1534 val_acc=0.9560
Epoch 12/100 | train_loss=0.0153 train_acc=0.9954 | val_loss=0.1421 val_acc=0.9560
Epoch 13/100 | train_loss=0.0073 train_acc=0.9969 | val_loss=0.1248 val_acc=0.9653
Epoch 14/100 | train_loss=0.0069 train_acc=0.9986 | val_loss=0.1021 val_acc=0.9733
Epoch 15/100 | train_loss=0.0097 train_acc=0.9977 | val_loss=0.1169 val_acc=0.9733
Epoch 16/100 | train_loss=0.0040 train_acc=0.9989 | val_loss=0.1195 val_acc=0.9640
Epoch 17/100 | train_loss=0.0072 train_acc=0.9980 | val_loss=0.1142 val_acc=0.9733
Epoch 18/100 | train_loss=0.0045 train_acc=0.9986 | val_loss=0.0826 val_acc=0.9773
Epoch 19/100 | train_loss=0.0107 train_acc=0.9957 | val_loss=0.1294 val_acc=0.9627
Epoch 20/100 | train_loss=0.0033 train_acc=0.9991 | val_loss=0.1482 val_acc=0.9627
Epoch 21/100 | train_loss=0.0012 train_acc=1.0000 | val_loss=0.1844 val_acc=0.9547
Epoch 22/100 | train_loss=0.0020 train_acc=0.9991 | val_loss=0.1287 val_acc=0.9680
Epoch 23/100 | train_loss=0.0011 train_acc=0.9997 | val_loss=0.1380 val_acc=0.9653
Epoch 24/100 | train_loss=0.0044 train_acc=0.9983 | val_loss=0.1261 val_acc=0.9720
Epoch 25/100 | train_loss=0.0194 train_acc=0.9940 | val_loss=0.1356 val_acc=0.9640
Epoch 26/100 | train_loss=0.0093 train_acc=0.9974 | val_loss=0.0730 val_acc=0.9787
Epoch 27/100 | train_loss=0.0502 train_acc=0.9854 | val_loss=0.1704 val_acc=0.9667
Epoch 28/100 | train_loss=0.0144 train_acc=0.9949 | val_loss=0.1385 val_acc=0.9680
Epoch 29/100 | train_loss=0.0069 train_acc=0.9966 | val_loss=0.1218 val_acc=0.9813
Epoch 30/100 | train_loss=0.0030 train_acc=0.9980 | val_loss=0.1223 val_acc=0.9800
Epoch 31/100 | train_loss=0.0034 train_acc=0.9989 | val_loss=0.1417 val_acc=0.9720
Epoch 32/100 | train_loss=0.0043 train_acc=0.9986 | val_loss=0.1183 val_acc=0.9733
Epoch 33/100 | train_loss=0.0025 train_acc=0.9994 | val_loss=0.1139 val_acc=0.9800
Epoch 34/100 | train_loss=0.0034 train_acc=0.9986 | val_loss=0.1199 val_acc=0.9800
Epoch 35/100 | train_loss=0.0023 train_acc=0.9994 | val_loss=0.1493 val_acc=0.9733
Epoch 36/100 | train_loss=0.0005 train_acc=1.0000 | val_loss=0.1383 val_acc=0.9760
Epoch 37/100 | train_loss=0.0002 train_acc=1.0000 | val_loss=0.1204 val_acc=0.9787
Epoch 38/100 | train_loss=0.0002 train_acc=1.0000 | val_loss=0.1078 val_acc=0.9813
Epoch 39/100 | train_loss=0.0054 train_acc=0.9986 | val_loss=0.2206 val_acc=0.9547
Epoch 40/100 | train_loss=0.0010 train_acc=0.9997 | val_loss=0.1360 val_acc=0.9760
Epoch 41/100 | train_loss=0.0004 train_acc=1.0000 | val_loss=0.1330 val_acc=0.9773
Epoch 42/100 | train_loss=0.0016 train_acc=0.9994 | val_loss=0.0445 val_acc=0.9867
Epoch 43/100 | train_loss=0.0183 train_acc=0.9960 | val_loss=0.1249 val_acc=0.9680
Epoch 44/100 | train_loss=0.0258 train_acc=0.9934 | val_loss=0.0546 val_acc=0.9853
Epoch 45/100 | train_loss=0.0137 train_acc=0.9949 | val_loss=0.0698 val_acc=0.9800
Epoch 46/100 | train_loss=0.0051 train_acc=0.9986 | val_loss=0.0461 val_acc=0.9840
Epoch 47/100 | train_loss=0.0032 train_acc=0.9991 | val_loss=0.0969 val_acc=0.9773
Epoch 48/100 | train_loss=0.0024 train_acc=0.9991 | val_loss=0.0575 val_acc=0.9867
Epoch 49/100 | train_loss=0.0047 train_acc=0.9986 | val_loss=0.0676 val_acc=0.9840
Epoch 50/100 | train_loss=0.0028 train_acc=0.9986 | val_loss=0.0837 val_acc=0.9773
Epoch 51/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0492 val_acc=0.9840
Epoch 52/100 | train_loss=0.0005 train_acc=1.0000 | val_loss=0.0888 val_acc=0.9760
Epoch 53/100 | train_loss=0.0027 train_acc=0.9989 | val_loss=0.0826 val_acc=0.9733
Epoch 54/100 | train_loss=0.0015 train_acc=0.9991 | val_loss=0.0855 val_acc=0.9760
Epoch 55/100 | train_loss=0.0089 train_acc=0.9971 | val_loss=0.1196 val_acc=0.9693
Epoch 56/100 | train_loss=0.0057 train_acc=0.9977 | val_loss=0.1028 val_acc=0.9680
Epoch 57/100 | train_loss=0.0012 train_acc=0.9997 | val_loss=0.1047 val_acc=0.9693
Epoch 58/100 | train_loss=0.0032 train_acc=0.9991 | val_loss=0.1845 val_acc=0.9493
Epoch 59/100 | train_loss=0.0037 train_acc=0.9991 | val_loss=0.0648 val_acc=0.9800
Epoch 60/100 | train_loss=0.0010 train_acc=0.9997 | val_loss=0.0516 val_acc=0.9853
Epoch 61/100 | train_loss=0.0077 train_acc=0.9977 | val_loss=0.0366 val_acc=0.9867
Epoch 62/100 | train_loss=0.0030 train_acc=0.9991 | val_loss=0.0783 val_acc=0.9787
Epoch 63/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0435 val_acc=0.9933
Epoch 64/100 | train_loss=0.0128 train_acc=0.9951 | val_loss=0.1272 val_acc=0.9707
Epoch 65/100 | train_loss=0.0107 train_acc=0.9957 | val_loss=0.0579 val_acc=0.9787
Epoch 66/100 | train_loss=0.0154 train_acc=0.9951 | val_loss=0.1661 val_acc=0.9547
Epoch 67/100 | train_loss=0.0042 train_acc=0.9983 | val_loss=0.0695 val_acc=0.9827
Epoch 68/100 | train_loss=0.0118 train_acc=0.9966 | val_loss=0.0518 val_acc=0.9853
Epoch 69/100 | train_loss=0.0062 train_acc=0.9974 | val_loss=0.0376 val_acc=0.9880
Epoch 70/100 | train_loss=0.0101 train_acc=0.9986 | val_loss=0.0608 val_acc=0.9800
Epoch 71/100 | train_loss=0.0014 train_acc=0.9997 | val_loss=0.0435 val_acc=0.9867
Epoch 72/100 | train_loss=0.0011 train_acc=0.9997 | val_loss=0.0283 val_acc=0.9893
Epoch 73/100 | train_loss=0.0060 train_acc=0.9977 | val_loss=0.0316 val_acc=0.9893
Epoch 74/100 | train_loss=0.0008 train_acc=0.9997 | val_loss=0.0301 val_acc=0.9880
Epoch 75/100 | train_loss=0.0015 train_acc=0.9994 | val_loss=0.0316 val_acc=0.9907
Epoch 76/100 | train_loss=0.0007 train_acc=0.9997 | val_loss=0.0651 val_acc=0.9813
Epoch 77/100 | train_loss=0.0021 train_acc=0.9994 | val_loss=0.0363 val_acc=0.9893
Epoch 78/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0343 val_acc=0.9920
Epoch 79/100 | train_loss=0.0031 train_acc=0.9989 | val_loss=0.0677 val_acc=0.9907
Epoch 80/100 | train_loss=0.0027 train_acc=0.9989 | val_loss=0.0463 val_acc=0.9880
Epoch 81/100 | train_loss=0.0024 train_acc=0.9991 | val_loss=0.0839 val_acc=0.9707
Epoch 82/100 | train_loss=0.0037 train_acc=0.9977 | val_loss=0.0617 val_acc=0.9787
Epoch 83/100 | train_loss=0.0097 train_acc=0.9971 | val_loss=0.0335 val_acc=0.9907
Epoch 84/100 | train_loss=0.0036 train_acc=0.9986 | val_loss=0.0535 val_acc=0.9853
Epoch 85/100 | train_loss=0.0007 train_acc=0.9997 | val_loss=0.0165 val_acc=0.9933
Epoch 86/100 | train_loss=0.0002 train_acc=1.0000 | val_loss=0.0102 val_acc=0.9947
Epoch 87/100 | train_loss=0.0000 train_acc=1.0000 | val_loss=0.0143 val_acc=0.9933
Epoch 88/100 | train_loss=0.0008 train_acc=0.9997 | val_loss=0.0346 val_acc=0.9880
Epoch 89/100 | train_loss=0.0059 train_acc=0.9991 | val_loss=0.0224 val_acc=0.9920
Epoch 90/100 | train_loss=0.0017 train_acc=0.9991 | val_loss=0.0251 val_acc=0.9907
Epoch 91/100 | train_loss=0.0103 train_acc=0.9969 | val_loss=0.0785 val_acc=0.9840
Epoch 92/100 | train_loss=0.0107 train_acc=0.9963 | val_loss=0.0658 val_acc=0.9853
Epoch 93/100 | train_loss=0.0031 train_acc=0.9986 | val_loss=0.0381 val_acc=0.9920
Epoch 94/100 | train_loss=0.0012 train_acc=0.9994 | val_loss=0.0277 val_acc=0.9933
Epoch 95/100 | train_loss=0.0018 train_acc=0.9997 | val_loss=0.0699 val_acc=0.9827
Epoch 96/100 | train_loss=0.0029 train_acc=0.9991 | val_loss=0.0294 val_acc=0.9907
Epoch 97/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0279 val_acc=0.9880
Epoch 98/100 | train_loss=0.0024 train_acc=0.9994 | val_loss=0.0437 val_acc=0.9867
Epoch 99/100 | train_loss=0.0001 train_acc=1.0000 | val_loss=0.0429 val_acc=0.9867
Epoch 100/100 | train_loss=0.0001 train_acc=1.0000 | val_loss=0.0201 val_acc=0.9933

Evaluating on test set...
Figure(400x400)
Figure(1200x450)

Done. Results saved to: /content/drive/MyDrive/diffusion_project/results/efficientnetv2s/results.json
Checkpoint saved to: /content/drive/MyDrive/diffusion_project/results/efficientnetv2s/checkpoint.pth

Summary — efficientnetv2s:
  Test Accuracy:  0.9960
  Test Precision: 0.9947
  Test Recall:    0.9973
  Test F1:        0.9960
  Parameters:     20,180,050
  Model size:     78.16 MB
  Avg latency:    3.75 ms/image

shufflenetv2:
Using device: cuda
Classes: ['ai', 'nature']
Downloading: "https://download.pytorch.org/models/shufflenetv2_x1-5666bf0f80.pth" to /root/.cache/torch/hub/checkpoints/shufflenetv2_x1-5666bf0f80.pth
100% 8.79M/8.79M [00:00<00:00, 118MB/s]
Epoch 1/100 | train_loss=0.6328 train_acc=0.7626 | val_loss=0.4885 val_acc=0.8440
Epoch 2/100 | train_loss=0.3744 train_acc=0.8903 | val_loss=0.2571 val_acc=0.9227
Epoch 3/100 | train_loss=0.2094 train_acc=0.9369 | val_loss=0.1494 val_acc=0.9640
Epoch 4/100 | train_loss=0.1364 train_acc=0.9583 | val_loss=0.1285 val_acc=0.9573
Epoch 5/100 | train_loss=0.0923 train_acc=0.9717 | val_loss=0.1304 val_acc=0.9533
Epoch 6/100 | train_loss=0.0702 train_acc=0.9786 | val_loss=0.0968 val_acc=0.9627
Epoch 7/100 | train_loss=0.0632 train_acc=0.9803 | val_loss=0.0785 val_acc=0.9693
Epoch 8/100 | train_loss=0.0677 train_acc=0.9766 | val_loss=0.1053 val_acc=0.9547
Epoch 9/100 | train_loss=0.0511 train_acc=0.9829 | val_loss=0.1059 val_acc=0.9560
Epoch 10/100 | train_loss=0.0336 train_acc=0.9903 | val_loss=0.0781 val_acc=0.9720
Epoch 11/100 | train_loss=0.0376 train_acc=0.9900 | val_loss=0.0709 val_acc=0.9733
Epoch 12/100 | train_loss=0.0293 train_acc=0.9917 | val_loss=0.1249 val_acc=0.9560
Epoch 13/100 | train_loss=0.0235 train_acc=0.9937 | val_loss=0.0800 val_acc=0.9760
Epoch 14/100 | train_loss=0.0340 train_acc=0.9869 | val_loss=0.1262 val_acc=0.9587
Epoch 15/100 | train_loss=0.0282 train_acc=0.9900 | val_loss=0.0839 val_acc=0.9667
Epoch 16/100 | train_loss=0.0233 train_acc=0.9931 | val_loss=0.0902 val_acc=0.9693
Epoch 17/100 | train_loss=0.0248 train_acc=0.9911 | val_loss=0.0858 val_acc=0.9707
Epoch 18/100 | train_loss=0.0259 train_acc=0.9926 | val_loss=0.1244 val_acc=0.9587
Epoch 19/100 | train_loss=0.0170 train_acc=0.9943 | val_loss=0.0786 val_acc=0.9773
Epoch 20/100 | train_loss=0.0146 train_acc=0.9951 | val_loss=0.1257 val_acc=0.9587
Epoch 21/100 | train_loss=0.0176 train_acc=0.9943 | val_loss=0.0850 val_acc=0.9733
Epoch 22/100 | train_loss=0.0194 train_acc=0.9937 | val_loss=0.0771 val_acc=0.9787
Epoch 23/100 | train_loss=0.0145 train_acc=0.9960 | val_loss=0.1304 val_acc=0.9613
Epoch 24/100 | train_loss=0.0144 train_acc=0.9946 | val_loss=0.0792 val_acc=0.9800
Epoch 25/100 | train_loss=0.0218 train_acc=0.9926 | val_loss=0.0914 val_acc=0.9720
Epoch 26/100 | train_loss=0.0149 train_acc=0.9969 | val_loss=0.0735 val_acc=0.9773
Epoch 27/100 | train_loss=0.0112 train_acc=0.9966 | val_loss=0.0756 val_acc=0.9747
Epoch 28/100 | train_loss=0.0143 train_acc=0.9960 | val_loss=0.0873 val_acc=0.9747
Epoch 29/100 | train_loss=0.0170 train_acc=0.9929 | val_loss=0.1082 val_acc=0.9680
Epoch 30/100 | train_loss=0.0106 train_acc=0.9966 | val_loss=0.1183 val_acc=0.9653
Epoch 31/100 | train_loss=0.0102 train_acc=0.9966 | val_loss=0.1132 val_acc=0.9680
Epoch 32/100 | train_loss=0.0094 train_acc=0.9969 | val_loss=0.1082 val_acc=0.9733
Epoch 33/100 | train_loss=0.0062 train_acc=0.9989 | val_loss=0.0996 val_acc=0.9733
Epoch 34/100 | train_loss=0.0093 train_acc=0.9974 | val_loss=0.0769 val_acc=0.9813
Epoch 35/100 | train_loss=0.0093 train_acc=0.9966 | val_loss=0.1042 val_acc=0.9693
Epoch 36/100 | train_loss=0.0109 train_acc=0.9974 | val_loss=0.1029 val_acc=0.9707
Epoch 37/100 | train_loss=0.0090 train_acc=0.9977 | val_loss=0.0813 val_acc=0.9800
Epoch 38/100 | train_loss=0.0059 train_acc=0.9986 | val_loss=0.0921 val_acc=0.9733
Epoch 39/100 | train_loss=0.0053 train_acc=0.9983 | val_loss=0.0824 val_acc=0.9773
Epoch 40/100 | train_loss=0.0055 train_acc=0.9983 | val_loss=0.0859 val_acc=0.9720
Epoch 41/100 | train_loss=0.0072 train_acc=0.9977 | val_loss=0.1033 val_acc=0.9707
Epoch 42/100 | train_loss=0.0062 train_acc=0.9980 | val_loss=0.1044 val_acc=0.9680
Epoch 43/100 | train_loss=0.0021 train_acc=1.0000 | val_loss=0.1044 val_acc=0.9680
Epoch 44/100 | train_loss=0.0094 train_acc=0.9969 | val_loss=0.0892 val_acc=0.9747
Epoch 45/100 | train_loss=0.0058 train_acc=0.9983 | val_loss=0.0847 val_acc=0.9733
Epoch 46/100 | train_loss=0.0097 train_acc=0.9969 | val_loss=0.0949 val_acc=0.9707
Epoch 47/100 | train_loss=0.0118 train_acc=0.9957 | val_loss=0.0989 val_acc=0.9747
Epoch 48/100 | train_loss=0.0097 train_acc=0.9974 | val_loss=0.1075 val_acc=0.9680
Epoch 49/100 | train_loss=0.0069 train_acc=0.9971 | val_loss=0.1201 val_acc=0.9733
Epoch 50/100 | train_loss=0.0039 train_acc=0.9986 | val_loss=0.1049 val_acc=0.9773
Epoch 51/100 | train_loss=0.0074 train_acc=0.9986 | val_loss=0.1247 val_acc=0.9667
Epoch 52/100 | train_loss=0.0048 train_acc=0.9977 | val_loss=0.1176 val_acc=0.9707
Epoch 53/100 | train_loss=0.0099 train_acc=0.9966 | val_loss=0.1152 val_acc=0.9680
Epoch 54/100 | train_loss=0.0043 train_acc=0.9989 | val_loss=0.0939 val_acc=0.9787
Epoch 55/100 | train_loss=0.0058 train_acc=0.9989 | val_loss=0.1010 val_acc=0.9773
Epoch 56/100 | train_loss=0.0043 train_acc=0.9989 | val_loss=0.1053 val_acc=0.9773
Epoch 57/100 | train_loss=0.0014 train_acc=1.0000 | val_loss=0.0832 val_acc=0.9827
Epoch 58/100 | train_loss=0.0111 train_acc=0.9963 | val_loss=0.1030 val_acc=0.9773
Epoch 59/100 | train_loss=0.0046 train_acc=0.9986 | val_loss=0.0744 val_acc=0.9813
Epoch 60/100 | train_loss=0.0058 train_acc=0.9989 | val_loss=0.0854 val_acc=0.9787
Epoch 61/100 | train_loss=0.0059 train_acc=0.9980 | val_loss=0.0649 val_acc=0.9840
Epoch 62/100 | train_loss=0.0070 train_acc=0.9974 | val_loss=0.0976 val_acc=0.9747
Epoch 63/100 | train_loss=0.0059 train_acc=0.9974 | val_loss=0.0778 val_acc=0.9813
Epoch 64/100 | train_loss=0.0139 train_acc=0.9957 | val_loss=0.1316 val_acc=0.9680
Epoch 65/100 | train_loss=0.0088 train_acc=0.9971 | val_loss=0.0703 val_acc=0.9813
Epoch 66/100 | train_loss=0.0061 train_acc=0.9977 | val_loss=0.0944 val_acc=0.9733
Epoch 67/100 | train_loss=0.0037 train_acc=0.9991 | val_loss=0.0941 val_acc=0.9773
Epoch 68/100 | train_loss=0.0035 train_acc=0.9994 | val_loss=0.0803 val_acc=0.9773
Epoch 69/100 | train_loss=0.0014 train_acc=0.9997 | val_loss=0.0857 val_acc=0.9800
Epoch 70/100 | train_loss=0.0033 train_acc=0.9989 | val_loss=0.1164 val_acc=0.9747
Epoch 71/100 | train_loss=0.0031 train_acc=0.9991 | val_loss=0.0936 val_acc=0.9773
Epoch 72/100 | train_loss=0.0027 train_acc=0.9991 | val_loss=0.1429 val_acc=0.9640
Epoch 73/100 | train_loss=0.0038 train_acc=0.9983 | val_loss=0.1019 val_acc=0.9720
Epoch 74/100 | train_loss=0.0100 train_acc=0.9977 | val_loss=0.1166 val_acc=0.9680
Epoch 75/100 | train_loss=0.0033 train_acc=0.9991 | val_loss=0.1023 val_acc=0.9707
Epoch 76/100 | train_loss=0.0065 train_acc=0.9980 | val_loss=0.1190 val_acc=0.9680
Epoch 77/100 | train_loss=0.0043 train_acc=0.9986 | val_loss=0.1227 val_acc=0.9667
Epoch 78/100 | train_loss=0.0050 train_acc=0.9986 | val_loss=0.1696 val_acc=0.9573
Epoch 79/100 | train_loss=0.0053 train_acc=0.9983 | val_loss=0.0853 val_acc=0.9773
Epoch 80/100 | train_loss=0.0020 train_acc=0.9997 | val_loss=0.0839 val_acc=0.9773
Epoch 81/100 | train_loss=0.0029 train_acc=0.9994 | val_loss=0.0942 val_acc=0.9733
Epoch 82/100 | train_loss=0.0051 train_acc=0.9977 | val_loss=0.1110 val_acc=0.9693
Epoch 83/100 | train_loss=0.0033 train_acc=0.9994 | val_loss=0.0695 val_acc=0.9827
Epoch 84/100 | train_loss=0.0073 train_acc=0.9977 | val_loss=0.1039 val_acc=0.9747
Epoch 85/100 | train_loss=0.0072 train_acc=0.9977 | val_loss=0.1102 val_acc=0.9733
Epoch 86/100 | train_loss=0.0032 train_acc=0.9989 | val_loss=0.1273 val_acc=0.9680
Epoch 87/100 | train_loss=0.0033 train_acc=0.9989 | val_loss=0.0808 val_acc=0.9853
Epoch 88/100 | train_loss=0.0051 train_acc=0.9980 | val_loss=0.1204 val_acc=0.9680
Epoch 89/100 | train_loss=0.0067 train_acc=0.9971 | val_loss=0.0773 val_acc=0.9813
Epoch 90/100 | train_loss=0.0047 train_acc=0.9989 | val_loss=0.1192 val_acc=0.9653
Epoch 91/100 | train_loss=0.0016 train_acc=0.9997 | val_loss=0.1066 val_acc=0.9733
Epoch 92/100 | train_loss=0.0011 train_acc=0.9997 | val_loss=0.1144 val_acc=0.9747
Epoch 93/100 | train_loss=0.0012 train_acc=0.9997 | val_loss=0.0982 val_acc=0.9800
Epoch 94/100 | train_loss=0.0016 train_acc=0.9994 | val_loss=0.0948 val_acc=0.9813
Epoch 95/100 | train_loss=0.0026 train_acc=0.9994 | val_loss=0.0788 val_acc=0.9827
Epoch 96/100 | train_loss=0.0053 train_acc=0.9977 | val_loss=0.1012 val_acc=0.9787
Epoch 97/100 | train_loss=0.0030 train_acc=0.9994 | val_loss=0.0823 val_acc=0.9840
Epoch 98/100 | train_loss=0.0018 train_acc=0.9994 | val_loss=0.1041 val_acc=0.9773
Epoch 99/100 | train_loss=0.0023 train_acc=0.9994 | val_loss=0.1261 val_acc=0.9707
Epoch 100/100 | train_loss=0.0025 train_acc=0.9994 | val_loss=0.0954 val_acc=0.9800

Evaluating on test set...
Figure(400x400)
Figure(1200x450)

Done. Results saved to: /content/drive/MyDrive/diffusion_project/results/shufflenetv2/results.json
Checkpoint saved to: /content/drive/MyDrive/diffusion_project/results/shufflenetv2/checkpoint.pth

Summary — shufflenetv2:
  Test Accuracy:  0.9853
  Test Precision: 0.9789
  Test Recall:    0.9920
  Test F1:        0.9854
  Parameters:     1,255,654
  Model size:     4.97 MB
  Avg latency:    0.50 ms/image

ghostnet:
Using device: cuda
Classes: ['ai', 'nature']
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.

model.safetensors: downloading bytes:  61% 12.7M/20.9M [00:01<00:00, 17.9MB/s,  301kB/s  ]
model.safetensors: downloading bytes: 100% 20.0M/20.0M [00:01<00:00, 15.5MB/s, 1.93MB/s  ]
model.safetensors: reconstructing file: 100% 20.9M/20.9M [00:01<00:00, 16.2MB/s, 2.03MB/s  ]
Epoch 1/100 | train_loss=0.5028 train_acc=0.7623 | val_loss=0.4440 val_acc=0.7600
Epoch 2/100 | train_loss=0.1969 train_acc=0.9220 | val_loss=0.2256 val_acc=0.9013
Epoch 3/100 | train_loss=0.1037 train_acc=0.9623 | val_loss=0.1635 val_acc=0.9333
Epoch 4/100 | train_loss=0.0768 train_acc=0.9691 | val_loss=0.1768 val_acc=0.9280
Epoch 5/100 | train_loss=0.0474 train_acc=0.9809 | val_loss=0.1329 val_acc=0.9453
Epoch 6/100 | train_loss=0.0586 train_acc=0.9794 | val_loss=0.1491 val_acc=0.9400
Epoch 7/100 | train_loss=0.0360 train_acc=0.9886 | val_loss=0.1048 val_acc=0.9640
Epoch 8/100 | train_loss=0.0328 train_acc=0.9900 | val_loss=0.0846 val_acc=0.9653
Epoch 9/100 | train_loss=0.0292 train_acc=0.9894 | val_loss=0.0833 val_acc=0.9787
Epoch 10/100 | train_loss=0.0224 train_acc=0.9926 | val_loss=0.1240 val_acc=0.9547
Epoch 11/100 | train_loss=0.0186 train_acc=0.9940 | val_loss=0.1569 val_acc=0.9480
Epoch 12/100 | train_loss=0.0255 train_acc=0.9926 | val_loss=0.1646 val_acc=0.9440
Epoch 13/100 | train_loss=0.0109 train_acc=0.9960 | val_loss=0.1613 val_acc=0.9493
Epoch 14/100 | train_loss=0.0124 train_acc=0.9957 | val_loss=0.1473 val_acc=0.9587
Epoch 15/100 | train_loss=0.0098 train_acc=0.9971 | val_loss=0.1123 val_acc=0.9640
Epoch 16/100 | train_loss=0.0078 train_acc=0.9977 | val_loss=0.1055 val_acc=0.9627
Epoch 17/100 | train_loss=0.0091 train_acc=0.9974 | val_loss=0.1735 val_acc=0.9560
Epoch 18/100 | train_loss=0.0120 train_acc=0.9951 | val_loss=0.1459 val_acc=0.9573
Epoch 19/100 | train_loss=0.0089 train_acc=0.9969 | val_loss=0.1203 val_acc=0.9653
Epoch 20/100 | train_loss=0.0041 train_acc=0.9991 | val_loss=0.1228 val_acc=0.9693
Epoch 21/100 | train_loss=0.0097 train_acc=0.9963 | val_loss=0.1812 val_acc=0.9560
Epoch 22/100 | train_loss=0.0085 train_acc=0.9974 | val_loss=0.1302 val_acc=0.9667
Epoch 23/100 | train_loss=0.0081 train_acc=0.9974 | val_loss=0.1345 val_acc=0.9613
Epoch 24/100 | train_loss=0.0100 train_acc=0.9974 | val_loss=0.1588 val_acc=0.9533
Epoch 25/100 | train_loss=0.0073 train_acc=0.9966 | val_loss=0.1485 val_acc=0.9547
Epoch 26/100 | train_loss=0.0094 train_acc=0.9960 | val_loss=0.1662 val_acc=0.9533
Epoch 27/100 | train_loss=0.0097 train_acc=0.9969 | val_loss=0.1709 val_acc=0.9480
Epoch 28/100 | train_loss=0.0050 train_acc=0.9983 | val_loss=0.1346 val_acc=0.9600
Epoch 29/100 | train_loss=0.0051 train_acc=0.9980 | val_loss=0.0886 val_acc=0.9707
Epoch 30/100 | train_loss=0.0072 train_acc=0.9977 | val_loss=0.1148 val_acc=0.9627
Epoch 31/100 | train_loss=0.0056 train_acc=0.9983 | val_loss=0.0731 val_acc=0.9787
Epoch 32/100 | train_loss=0.0057 train_acc=0.9986 | val_loss=0.0923 val_acc=0.9720
Epoch 33/100 | train_loss=0.0019 train_acc=0.9994 | val_loss=0.1225 val_acc=0.9587
Epoch 34/100 | train_loss=0.0016 train_acc=0.9994 | val_loss=0.1084 val_acc=0.9667
Epoch 35/100 | train_loss=0.0027 train_acc=0.9989 | val_loss=0.1264 val_acc=0.9667
Epoch 36/100 | train_loss=0.0038 train_acc=0.9980 | val_loss=0.2420 val_acc=0.9387
Epoch 37/100 | train_loss=0.0146 train_acc=0.9943 | val_loss=0.1476 val_acc=0.9587
Epoch 38/100 | train_loss=0.0096 train_acc=0.9974 | val_loss=0.0682 val_acc=0.9733
Epoch 39/100 | train_loss=0.0032 train_acc=0.9991 | val_loss=0.1116 val_acc=0.9600
Epoch 40/100 | train_loss=0.0049 train_acc=0.9980 | val_loss=0.0659 val_acc=0.9773
Epoch 41/100 | train_loss=0.0015 train_acc=1.0000 | val_loss=0.1023 val_acc=0.9680
Epoch 42/100 | train_loss=0.0047 train_acc=0.9986 | val_loss=0.1496 val_acc=0.9627
Epoch 43/100 | train_loss=0.0055 train_acc=0.9989 | val_loss=0.0929 val_acc=0.9760
Epoch 44/100 | train_loss=0.0038 train_acc=0.9983 | val_loss=0.1006 val_acc=0.9733
Epoch 45/100 | train_loss=0.0051 train_acc=0.9977 | val_loss=0.0801 val_acc=0.9813
Epoch 46/100 | train_loss=0.0032 train_acc=0.9997 | val_loss=0.1203 val_acc=0.9760
Epoch 47/100 | train_loss=0.0030 train_acc=0.9989 | val_loss=0.1195 val_acc=0.9693
Epoch 48/100 | train_loss=0.0014 train_acc=0.9994 | val_loss=0.1145 val_acc=0.9720
Epoch 49/100 | train_loss=0.0069 train_acc=0.9977 | val_loss=0.1605 val_acc=0.9560
Epoch 50/100 | train_loss=0.0049 train_acc=0.9980 | val_loss=0.1360 val_acc=0.9653
Epoch 51/100 | train_loss=0.0050 train_acc=0.9983 | val_loss=0.1301 val_acc=0.9640
Epoch 52/100 | train_loss=0.0022 train_acc=0.9994 | val_loss=0.1334 val_acc=0.9627
Epoch 53/100 | train_loss=0.0035 train_acc=0.9989 | val_loss=0.0894 val_acc=0.9707
Epoch 54/100 | train_loss=0.0017 train_acc=0.9997 | val_loss=0.0685 val_acc=0.9773
Epoch 55/100 | train_loss=0.0013 train_acc=0.9997 | val_loss=0.0873 val_acc=0.9773
Epoch 56/100 | train_loss=0.0019 train_acc=0.9991 | val_loss=0.0621 val_acc=0.9827
Epoch 57/100 | train_loss=0.0012 train_acc=0.9994 | val_loss=0.0783 val_acc=0.9813
Epoch 58/100 | train_loss=0.0027 train_acc=0.9991 | val_loss=0.1514 val_acc=0.9600
Epoch 59/100 | train_loss=0.0243 train_acc=0.9971 | val_loss=0.1029 val_acc=0.9707
Epoch 60/100 | train_loss=0.0234 train_acc=0.9911 | val_loss=0.2081 val_acc=0.9520
Epoch 61/100 | train_loss=0.0044 train_acc=0.9989 | val_loss=0.1619 val_acc=0.9560
Epoch 62/100 | train_loss=0.0062 train_acc=0.9977 | val_loss=0.1572 val_acc=0.9667
Epoch 63/100 | train_loss=0.0017 train_acc=0.9994 | val_loss=0.1624 val_acc=0.9653
Epoch 64/100 | train_loss=0.0026 train_acc=0.9994 | val_loss=0.1659 val_acc=0.9627
Epoch 65/100 | train_loss=0.0019 train_acc=0.9994 | val_loss=0.2109 val_acc=0.9560
Epoch 66/100 | train_loss=0.0014 train_acc=0.9994 | val_loss=0.1793 val_acc=0.9667
Epoch 67/100 | train_loss=0.0044 train_acc=0.9986 | val_loss=0.2045 val_acc=0.9613
Epoch 68/100 | train_loss=0.0055 train_acc=0.9977 | val_loss=0.1716 val_acc=0.9547
Epoch 69/100 | train_loss=0.0015 train_acc=0.9994 | val_loss=0.1476 val_acc=0.9587
Epoch 70/100 | train_loss=0.0008 train_acc=1.0000 | val_loss=0.1023 val_acc=0.9733
Epoch 71/100 | train_loss=0.0008 train_acc=0.9997 | val_loss=0.0871 val_acc=0.9693
Epoch 72/100 | train_loss=0.0006 train_acc=0.9997 | val_loss=0.1689 val_acc=0.9587
Epoch 73/100 | train_loss=0.0014 train_acc=0.9997 | val_loss=0.1607 val_acc=0.9653
Epoch 74/100 | train_loss=0.0019 train_acc=0.9989 | val_loss=0.1151 val_acc=0.9733
Epoch 75/100 | train_loss=0.0019 train_acc=0.9991 | val_loss=0.1388 val_acc=0.9760
Epoch 76/100 | train_loss=0.0012 train_acc=0.9991 | val_loss=0.1222 val_acc=0.9720
Epoch 77/100 | train_loss=0.0025 train_acc=0.9994 | val_loss=0.1343 val_acc=0.9627
Epoch 78/100 | train_loss=0.0020 train_acc=0.9991 | val_loss=0.1330 val_acc=0.9773
Epoch 79/100 | train_loss=0.0030 train_acc=0.9989 | val_loss=0.1870 val_acc=0.9573
Epoch 80/100 | train_loss=0.0133 train_acc=0.9957 | val_loss=0.1426 val_acc=0.9733
Epoch 81/100 | train_loss=0.0025 train_acc=0.9989 | val_loss=0.0894 val_acc=0.9760
Epoch 82/100 | train_loss=0.0008 train_acc=0.9997 | val_loss=0.0783 val_acc=0.9773
Epoch 83/100 | train_loss=0.0010 train_acc=0.9997 | val_loss=0.0907 val_acc=0.9747
Epoch 84/100 | train_loss=0.0002 train_acc=1.0000 | val_loss=0.0965 val_acc=0.9773
Epoch 85/100 | train_loss=0.0004 train_acc=1.0000 | val_loss=0.0954 val_acc=0.9760
Epoch 86/100 | train_loss=0.0004 train_acc=1.0000 | val_loss=0.0725 val_acc=0.9787
Epoch 87/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.1027 val_acc=0.9813
Epoch 88/100 | train_loss=0.0010 train_acc=0.9997 | val_loss=0.1171 val_acc=0.9720
Epoch 89/100 | train_loss=0.0012 train_acc=0.9994 | val_loss=0.0931 val_acc=0.9760
Epoch 90/100 | train_loss=0.0015 train_acc=0.9991 | val_loss=0.0884 val_acc=0.9787
Epoch 91/100 | train_loss=0.0044 train_acc=0.9989 | val_loss=0.1369 val_acc=0.9627
Epoch 92/100 | train_loss=0.0237 train_acc=0.9934 | val_loss=0.1464 val_acc=0.9627
Epoch 93/100 | train_loss=0.0114 train_acc=0.9969 | val_loss=0.0971 val_acc=0.9707
Epoch 94/100 | train_loss=0.0043 train_acc=0.9983 | val_loss=0.0898 val_acc=0.9720
Epoch 95/100 | train_loss=0.0006 train_acc=1.0000 | val_loss=0.0729 val_acc=0.9773
Epoch 96/100 | train_loss=0.0015 train_acc=0.9997 | val_loss=0.0828 val_acc=0.9760
Epoch 97/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0843 val_acc=0.9773
Epoch 98/100 | train_loss=0.0028 train_acc=0.9994 | val_loss=0.1096 val_acc=0.9720
Epoch 99/100 | train_loss=0.0017 train_acc=0.9994 | val_loss=0.0674 val_acc=0.9800
Epoch 100/100 | train_loss=0.0009 train_acc=0.9997 | val_loss=0.1197 val_acc=0.9693

Evaluating on test set...
Figure(400x400)
Figure(1200x450)

Done. Results saved to: /content/drive/MyDrive/diffusion_project/results/ghostnet/results.json
Checkpoint saved to: /content/drive/MyDrive/diffusion_project/results/ghostnet/checkpoint.pth

Summary — ghostnet:
  Test Accuracy:  0.9720
  Test Precision: 0.9863
  Test Recall:    0.9573
  Test F1:        0.9716
  Parameters:     3,904,070
  Model size:     15.21 MB
  Avg latency:    0.89 ms/image

mobilenetv3small:
Using device: cuda
Classes: ['ai', 'nature']
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.

model.safetensors: downloading bytes:  23% 2.31M/10.2M [00:01<00:05, 1.42MB/s]
model.safetensors: downloading bytes: 100% 9.76M/9.76M [00:01<00:00, 5.66MB/s,  941kB/s  ]
model.safetensors: reconstructing file: 100% 10.2M/10.2M [00:01<00:00, 5.94MB/s,  989kB/s  ]
Epoch 1/100 | train_loss=1.3411 train_acc=0.7663 | val_loss=0.7179 val_acc=0.8227
Epoch 2/100 | train_loss=0.5833 train_acc=0.8589 | val_loss=0.5807 val_acc=0.8520
Epoch 3/100 | train_loss=0.3609 train_acc=0.9023 | val_loss=1.5059 val_acc=0.7560
Epoch 4/100 | train_loss=0.2315 train_acc=0.9274 | val_loss=0.6121 val_acc=0.8720
Epoch 5/100 | train_loss=0.2749 train_acc=0.9231 | val_loss=0.4127 val_acc=0.9013
Epoch 6/100 | train_loss=0.1565 train_acc=0.9449 | val_loss=0.3263 val_acc=0.9227
Epoch 7/100 | train_loss=0.1173 train_acc=0.9669 | val_loss=0.2038 val_acc=0.9267
Epoch 8/100 | train_loss=0.1394 train_acc=0.9534 | val_loss=0.2733 val_acc=0.9160
Epoch 9/100 | train_loss=0.1531 train_acc=0.9577 | val_loss=0.4494 val_acc=0.9027
Epoch 10/100 | train_loss=0.1013 train_acc=0.9640 | val_loss=0.2649 val_acc=0.9373
Epoch 11/100 | train_loss=0.0880 train_acc=0.9720 | val_loss=0.3074 val_acc=0.9413
Epoch 12/100 | train_loss=0.0937 train_acc=0.9714 | val_loss=0.4045 val_acc=0.9160
Epoch 13/100 | train_loss=0.1122 train_acc=0.9646 | val_loss=0.2502 val_acc=0.9493
Epoch 14/100 | train_loss=0.1029 train_acc=0.9706 | val_loss=0.2695 val_acc=0.9427
Epoch 15/100 | train_loss=0.0667 train_acc=0.9780 | val_loss=0.2985 val_acc=0.9307
Epoch 16/100 | train_loss=0.0736 train_acc=0.9797 | val_loss=0.1871 val_acc=0.9573
Epoch 17/100 | train_loss=0.1157 train_acc=0.9666 | val_loss=0.1814 val_acc=0.9573
Epoch 18/100 | train_loss=0.1169 train_acc=0.9643 | val_loss=0.4714 val_acc=0.9187
Epoch 19/100 | train_loss=0.1193 train_acc=0.9666 | val_loss=0.4878 val_acc=0.9293
Epoch 20/100 | train_loss=0.1249 train_acc=0.9689 | val_loss=0.8437 val_acc=0.8573
Epoch 21/100 | train_loss=0.0707 train_acc=0.9794 | val_loss=0.1376 val_acc=0.9667
Epoch 22/100 | train_loss=0.0263 train_acc=0.9914 | val_loss=0.2093 val_acc=0.9520
Epoch 23/100 | train_loss=0.0457 train_acc=0.9860 | val_loss=0.1637 val_acc=0.9573
Epoch 24/100 | train_loss=0.0589 train_acc=0.9829 | val_loss=0.3054 val_acc=0.9347
Epoch 25/100 | train_loss=0.0902 train_acc=0.9754 | val_loss=0.2298 val_acc=0.9387
Epoch 26/100 | train_loss=0.0238 train_acc=0.9891 | val_loss=0.3823 val_acc=0.9293
Epoch 27/100 | train_loss=0.0264 train_acc=0.9914 | val_loss=0.2636 val_acc=0.9307
Epoch 28/100 | train_loss=0.0306 train_acc=0.9886 | val_loss=0.1998 val_acc=0.9640
Epoch 29/100 | train_loss=0.0513 train_acc=0.9834 | val_loss=0.2858 val_acc=0.9373
Epoch 30/100 | train_loss=0.0745 train_acc=0.9763 | val_loss=0.1855 val_acc=0.9587
Epoch 31/100 | train_loss=0.0373 train_acc=0.9880 | val_loss=0.3858 val_acc=0.9093
Epoch 32/100 | train_loss=0.0439 train_acc=0.9863 | val_loss=0.4121 val_acc=0.9120
Epoch 33/100 | train_loss=0.0534 train_acc=0.9820 | val_loss=0.2079 val_acc=0.9547
Epoch 34/100 | train_loss=0.0459 train_acc=0.9854 | val_loss=0.1786 val_acc=0.9547
Epoch 35/100 | train_loss=0.0243 train_acc=0.9909 | val_loss=0.3097 val_acc=0.9427
Epoch 36/100 | train_loss=0.0479 train_acc=0.9817 | val_loss=0.2245 val_acc=0.9413
Epoch 37/100 | train_loss=0.0341 train_acc=0.9880 | val_loss=0.2872 val_acc=0.9400
Epoch 38/100 | train_loss=0.0396 train_acc=0.9860 | val_loss=0.2970 val_acc=0.9307
Epoch 39/100 | train_loss=0.0315 train_acc=0.9914 | val_loss=0.3019 val_acc=0.9400
Epoch 40/100 | train_loss=0.0595 train_acc=0.9823 | val_loss=0.2094 val_acc=0.9533
Epoch 41/100 | train_loss=0.0375 train_acc=0.9871 | val_loss=0.2092 val_acc=0.9587
Epoch 42/100 | train_loss=0.0549 train_acc=0.9829 | val_loss=0.4285 val_acc=0.9200
Epoch 43/100 | train_loss=0.1611 train_acc=0.9569 | val_loss=0.3729 val_acc=0.9360
Epoch 44/100 | train_loss=0.0931 train_acc=0.9723 | val_loss=0.3051 val_acc=0.9467
Epoch 45/100 | train_loss=0.0429 train_acc=0.9866 | val_loss=0.2187 val_acc=0.9493
Epoch 46/100 | train_loss=0.0307 train_acc=0.9897 | val_loss=0.2379 val_acc=0.9387
Epoch 47/100 | train_loss=0.0120 train_acc=0.9954 | val_loss=0.2549 val_acc=0.9480
Epoch 48/100 | train_loss=0.0229 train_acc=0.9920 | val_loss=0.2064 val_acc=0.9493
Epoch 49/100 | train_loss=0.0589 train_acc=0.9817 | val_loss=0.3480 val_acc=0.9467
Epoch 50/100 | train_loss=0.0344 train_acc=0.9903 | val_loss=0.2160 val_acc=0.9507
Epoch 51/100 | train_loss=0.0172 train_acc=0.9929 | val_loss=0.2979 val_acc=0.9360
Epoch 52/100 | train_loss=0.0229 train_acc=0.9926 | val_loss=0.2374 val_acc=0.9373
Epoch 53/100 | train_loss=0.0189 train_acc=0.9946 | val_loss=0.2074 val_acc=0.9573
Epoch 54/100 | train_loss=0.0166 train_acc=0.9949 | val_loss=0.1433 val_acc=0.9627
Epoch 55/100 | train_loss=0.0312 train_acc=0.9900 | val_loss=0.4067 val_acc=0.9173
Epoch 56/100 | train_loss=0.0197 train_acc=0.9926 | val_loss=0.2543 val_acc=0.9507
Epoch 57/100 | train_loss=0.0169 train_acc=0.9940 | val_loss=0.2143 val_acc=0.9587
Epoch 58/100 | train_loss=0.0226 train_acc=0.9934 | val_loss=0.2795 val_acc=0.9520
Epoch 59/100 | train_loss=0.1578 train_acc=0.9646 | val_loss=0.2398 val_acc=0.9467
Epoch 60/100 | train_loss=0.0645 train_acc=0.9800 | val_loss=0.2732 val_acc=0.9307
Epoch 61/100 | train_loss=0.0862 train_acc=0.9757 | val_loss=0.3229 val_acc=0.9400
Epoch 62/100 | train_loss=0.0341 train_acc=0.9894 | val_loss=0.1852 val_acc=0.9587
Epoch 63/100 | train_loss=0.0264 train_acc=0.9897 | val_loss=0.2019 val_acc=0.9600
Epoch 64/100 | train_loss=0.0177 train_acc=0.9940 | val_loss=0.1520 val_acc=0.9667
Epoch 65/100 | train_loss=0.0162 train_acc=0.9940 | val_loss=0.1629 val_acc=0.9613
Epoch 66/100 | train_loss=0.0159 train_acc=0.9951 | val_loss=0.1716 val_acc=0.9640
Epoch 67/100 | train_loss=0.0168 train_acc=0.9943 | val_loss=0.1703 val_acc=0.9680
Epoch 68/100 | train_loss=0.0096 train_acc=0.9971 | val_loss=0.3006 val_acc=0.9493
Epoch 69/100 | train_loss=0.0220 train_acc=0.9923 | val_loss=0.1907 val_acc=0.9627
Epoch 70/100 | train_loss=0.0106 train_acc=0.9969 | val_loss=0.2590 val_acc=0.9507
Epoch 71/100 | train_loss=0.0174 train_acc=0.9934 | val_loss=0.2268 val_acc=0.9520
Epoch 72/100 | train_loss=0.0400 train_acc=0.9860 | val_loss=0.7809 val_acc=0.8920
Epoch 73/100 | train_loss=0.0639 train_acc=0.9809 | val_loss=0.1619 val_acc=0.9600
Epoch 74/100 | train_loss=0.0476 train_acc=0.9817 | val_loss=1.0501 val_acc=0.8533
Epoch 75/100 | train_loss=0.0647 train_acc=0.9800 | val_loss=0.3082 val_acc=0.9453
Epoch 76/100 | train_loss=0.0327 train_acc=0.9914 | val_loss=0.1655 val_acc=0.9627
Epoch 77/100 | train_loss=0.0315 train_acc=0.9891 | val_loss=0.2297 val_acc=0.9480
Epoch 78/100 | train_loss=0.0166 train_acc=0.9949 | val_loss=0.2030 val_acc=0.9587
Epoch 79/100 | train_loss=0.0146 train_acc=0.9951 | val_loss=0.1781 val_acc=0.9573
Epoch 80/100 | train_loss=0.0137 train_acc=0.9954 | val_loss=0.3088 val_acc=0.9520
Epoch 81/100 | train_loss=0.0228 train_acc=0.9931 | val_loss=0.4347 val_acc=0.9200
Epoch 82/100 | train_loss=0.0146 train_acc=0.9963 | val_loss=0.1636 val_acc=0.9613
Epoch 83/100 | train_loss=0.0120 train_acc=0.9963 | val_loss=0.2286 val_acc=0.9587
Epoch 84/100 | train_loss=0.0271 train_acc=0.9923 | val_loss=0.3711 val_acc=0.9293
Epoch 85/100 | train_loss=0.0252 train_acc=0.9914 | val_loss=0.1707 val_acc=0.9627
Epoch 86/100 | train_loss=0.0164 train_acc=0.9940 | val_loss=0.2193 val_acc=0.9587
Epoch 87/100 | train_loss=0.0215 train_acc=0.9920 | val_loss=0.2283 val_acc=0.9533
Epoch 88/100 | train_loss=0.0318 train_acc=0.9903 | val_loss=0.2309 val_acc=0.9587
Epoch 89/100 | train_loss=0.0557 train_acc=0.9849 | val_loss=0.3052 val_acc=0.9480
Epoch 90/100 | train_loss=0.0139 train_acc=0.9957 | val_loss=0.1545 val_acc=0.9653
Epoch 91/100 | train_loss=0.0175 train_acc=0.9951 | val_loss=0.2872 val_acc=0.9573
Epoch 92/100 | train_loss=0.0120 train_acc=0.9963 | val_loss=0.2241 val_acc=0.9453
Epoch 93/100 | train_loss=0.0193 train_acc=0.9943 | val_loss=0.7911 val_acc=0.8867
Epoch 94/100 | train_loss=0.0654 train_acc=0.9811 | val_loss=0.1894 val_acc=0.9547
Epoch 95/100 | train_loss=0.0212 train_acc=0.9934 | val_loss=0.1951 val_acc=0.9680
Epoch 96/100 | train_loss=0.0192 train_acc=0.9937 | val_loss=0.2127 val_acc=0.9613
Epoch 97/100 | train_loss=0.0106 train_acc=0.9960 | val_loss=0.1940 val_acc=0.9653
Epoch 98/100 | train_loss=0.0043 train_acc=0.9989 | val_loss=0.2133 val_acc=0.9720
Epoch 99/100 | train_loss=0.0116 train_acc=0.9957 | val_loss=0.3236 val_acc=0.9373
Epoch 100/100 | train_loss=0.0118 train_acc=0.9963 | val_loss=0.1791 val_acc=0.9653

Evaluating on test set...
Figure(400x400)
Figure(1200x450)

Done. Results saved to: /content/drive/MyDrive/diffusion_project/results/mobilenetv3small/results.json
Checkpoint saved to: /content/drive/MyDrive/diffusion_project/results/mobilenetv3small/checkpoint.pth

Summary — mobilenetv3small:
  Test Accuracy:  0.9613
  Test Precision: 0.9806
  Test Recall:    0.9413
  Test F1:        0.9605
  Parameters:     1,519,906
  Model size:     6.02 MB
  Avg latency:    0.35 ms/image

resnet50:
Using device: cuda
Classes: ['ai', 'nature']
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.

model.safetensors: downloading bytes:   6% 5.83M/102M [00:00<00:12, 7.61MB/s]
model.safetensors: downloading bytes:  21% 21.8M/102M [00:00<00:02, 31.5MB/s,  576kB/s  ]
model.safetensors: downloading bytes:  36% 36.8M/102M [00:00<00:01, 53.1MB/s, 2.15MB/s  ]
model.safetensors: reconstructing file:  41% 41.8M/102M [00:01<00:01, 50.0MB/s, 2.99MB/s  ]
model.safetensors: downloading bytes:  58% 59.1M/102M [00:01<00:00, 72.9MB/s, 4.51MB/s  ]
model.safetensors: downloading bytes:  77% 78.9M/102M [00:01<00:00, 81.1MB/s, 6.64MB/s  ]
model.safetensors: downloading bytes: 100% 96.2M/96.2M [00:01<00:00, 57.5MB/s, 8.93MB/s  ]
model.safetensors: reconstructing file: 100% 102M/102M [00:01<00:00, 61.2MB/s, 9.55MB/s  ] 
Epoch 1/100 | train_loss=0.6336 train_acc=0.6711 | val_loss=0.5350 val_acc=0.8387
Epoch 2/100 | train_loss=0.3210 train_acc=0.9111 | val_loss=0.1134 val_acc=0.9733
Epoch 3/100 | train_loss=0.1211 train_acc=0.9606 | val_loss=0.0786 val_acc=0.9693
Epoch 4/100 | train_loss=0.0650 train_acc=0.9794 | val_loss=0.0675 val_acc=0.9720
Epoch 5/100 | train_loss=0.0467 train_acc=0.9860 | val_loss=0.0395 val_acc=0.9893
Epoch 6/100 | train_loss=0.0424 train_acc=0.9871 | val_loss=0.0242 val_acc=0.9933
Epoch 7/100 | train_loss=0.0393 train_acc=0.9877 | val_loss=0.0715 val_acc=0.9760
Epoch 8/100 | train_loss=0.0215 train_acc=0.9937 | val_loss=0.0144 val_acc=0.9947
Epoch 9/100 | train_loss=0.0267 train_acc=0.9929 | val_loss=0.0147 val_acc=0.9947
Epoch 10/100 | train_loss=0.0343 train_acc=0.9903 | val_loss=0.0295 val_acc=0.9907
Epoch 11/100 | train_loss=0.0281 train_acc=0.9914 | val_loss=0.0606 val_acc=0.9760
Epoch 12/100 | train_loss=0.0302 train_acc=0.9897 | val_loss=0.0120 val_acc=0.9960
Epoch 13/100 | train_loss=0.0149 train_acc=0.9943 | val_loss=0.0156 val_acc=0.9947
Epoch 14/100 | train_loss=0.0113 train_acc=0.9977 | val_loss=0.0092 val_acc=0.9973
Epoch 15/100 | train_loss=0.0120 train_acc=0.9966 | val_loss=0.0146 val_acc=0.9973
Epoch 16/100 | train_loss=0.0101 train_acc=0.9966 | val_loss=0.0134 val_acc=0.9960
Epoch 17/100 | train_loss=0.0096 train_acc=0.9980 | val_loss=0.0127 val_acc=0.9960
Epoch 18/100 | train_loss=0.0123 train_acc=0.9960 | val_loss=0.0173 val_acc=0.9920
Epoch 19/100 | train_loss=0.0137 train_acc=0.9949 | val_loss=0.0120 val_acc=0.9947
Epoch 20/100 | train_loss=0.0064 train_acc=0.9983 | val_loss=0.0113 val_acc=0.9960
Epoch 21/100 | train_loss=0.0048 train_acc=0.9983 | val_loss=0.0088 val_acc=0.9973
Epoch 22/100 | train_loss=0.0082 train_acc=0.9974 | val_loss=0.0131 val_acc=0.9973
Epoch 23/100 | train_loss=0.0103 train_acc=0.9969 | val_loss=0.0205 val_acc=0.9920
Epoch 24/100 | train_loss=0.0068 train_acc=0.9980 | val_loss=0.0236 val_acc=0.9920
Epoch 25/100 | train_loss=0.0059 train_acc=0.9983 | val_loss=0.0123 val_acc=0.9947
Epoch 26/100 | train_loss=0.0060 train_acc=0.9977 | val_loss=0.0158 val_acc=0.9933
Epoch 27/100 | train_loss=0.0036 train_acc=0.9989 | val_loss=0.0151 val_acc=0.9933
Epoch 28/100 | train_loss=0.0138 train_acc=0.9960 | val_loss=0.0165 val_acc=0.9947
Epoch 29/100 | train_loss=0.0023 train_acc=0.9997 | val_loss=0.0124 val_acc=0.9947
Epoch 30/100 | train_loss=0.0046 train_acc=0.9989 | val_loss=0.0130 val_acc=0.9947
Epoch 31/100 | train_loss=0.0013 train_acc=1.0000 | val_loss=0.0073 val_acc=0.9960
Epoch 32/100 | train_loss=0.0026 train_acc=0.9994 | val_loss=0.0195 val_acc=0.9947
Epoch 33/100 | train_loss=0.0018 train_acc=0.9997 | val_loss=0.0097 val_acc=0.9947
Epoch 34/100 | train_loss=0.0054 train_acc=0.9977 | val_loss=0.0173 val_acc=0.9920
Epoch 35/100 | train_loss=0.0023 train_acc=0.9997 | val_loss=0.0129 val_acc=0.9933
Epoch 36/100 | train_loss=0.0019 train_acc=0.9991 | val_loss=0.0141 val_acc=0.9933
Epoch 37/100 | train_loss=0.0018 train_acc=0.9997 | val_loss=0.0100 val_acc=0.9987
Epoch 38/100 | train_loss=0.0015 train_acc=0.9997 | val_loss=0.0102 val_acc=0.9960
Epoch 39/100 | train_loss=0.0015 train_acc=0.9997 | val_loss=0.0094 val_acc=0.9973
Epoch 40/100 | train_loss=0.0018 train_acc=0.9994 | val_loss=0.0341 val_acc=0.9907
Epoch 41/100 | train_loss=0.0030 train_acc=0.9989 | val_loss=0.0212 val_acc=0.9920
Epoch 42/100 | train_loss=0.0050 train_acc=0.9977 | val_loss=0.0121 val_acc=0.9960
Epoch 43/100 | train_loss=0.0010 train_acc=1.0000 | val_loss=0.0120 val_acc=0.9947
Epoch 44/100 | train_loss=0.0007 train_acc=1.0000 | val_loss=0.0155 val_acc=0.9960
Epoch 45/100 | train_loss=0.0059 train_acc=0.9977 | val_loss=0.0445 val_acc=0.9880
Epoch 46/100 | train_loss=0.0014 train_acc=1.0000 | val_loss=0.0314 val_acc=0.9920
Epoch 47/100 | train_loss=0.0004 train_acc=1.0000 | val_loss=0.0308 val_acc=0.9920
Epoch 48/100 | train_loss=0.0018 train_acc=0.9994 | val_loss=0.0331 val_acc=0.9907
Epoch 49/100 | train_loss=0.0004 train_acc=1.0000 | val_loss=0.0322 val_acc=0.9920
Epoch 50/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0340 val_acc=0.9933
Epoch 51/100 | train_loss=0.0005 train_acc=1.0000 | val_loss=0.0412 val_acc=0.9907
Epoch 52/100 | train_loss=0.0088 train_acc=0.9966 | val_loss=0.0423 val_acc=0.9880
Epoch 53/100 | train_loss=0.0016 train_acc=0.9997 | val_loss=0.0306 val_acc=0.9920
Epoch 54/100 | train_loss=0.0024 train_acc=0.9994 | val_loss=0.0723 val_acc=0.9787
Epoch 55/100 | train_loss=0.0074 train_acc=0.9983 | val_loss=0.0413 val_acc=0.9867
Epoch 56/100 | train_loss=0.0012 train_acc=0.9997 | val_loss=0.0260 val_acc=0.9907
Epoch 57/100 | train_loss=0.0014 train_acc=0.9994 | val_loss=0.0244 val_acc=0.9920
Epoch 58/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0194 val_acc=0.9893
Epoch 59/100 | train_loss=0.0020 train_acc=0.9991 | val_loss=0.0304 val_acc=0.9933
Epoch 60/100 | train_loss=0.0026 train_acc=0.9997 | val_loss=0.0217 val_acc=0.9920
Epoch 61/100 | train_loss=0.0010 train_acc=1.0000 | val_loss=0.0306 val_acc=0.9867
Epoch 62/100 | train_loss=0.0012 train_acc=0.9997 | val_loss=0.0255 val_acc=0.9907
Epoch 63/100 | train_loss=0.0044 train_acc=0.9983 | val_loss=0.0242 val_acc=0.9933
Epoch 64/100 | train_loss=0.0040 train_acc=0.9994 | val_loss=0.0244 val_acc=0.9907
Epoch 65/100 | train_loss=0.0059 train_acc=0.9974 | val_loss=0.0306 val_acc=0.9907
Epoch 66/100 | train_loss=0.0016 train_acc=0.9994 | val_loss=0.0200 val_acc=0.9907
Epoch 67/100 | train_loss=0.0007 train_acc=1.0000 | val_loss=0.0137 val_acc=0.9933
Epoch 68/100 | train_loss=0.0007 train_acc=0.9997 | val_loss=0.0229 val_acc=0.9907
Epoch 69/100 | train_loss=0.0030 train_acc=0.9989 | val_loss=0.0180 val_acc=0.9947
Epoch 70/100 | train_loss=0.0005 train_acc=1.0000 | val_loss=0.0149 val_acc=0.9960
Epoch 71/100 | train_loss=0.0007 train_acc=1.0000 | val_loss=0.0149 val_acc=0.9960
Epoch 72/100 | train_loss=0.0011 train_acc=0.9997 | val_loss=0.0142 val_acc=0.9973
Epoch 73/100 | train_loss=0.0005 train_acc=0.9997 | val_loss=0.0227 val_acc=0.9920
Epoch 74/100 | train_loss=0.0006 train_acc=0.9997 | val_loss=0.0161 val_acc=0.9947
Epoch 75/100 | train_loss=0.0009 train_acc=0.9997 | val_loss=0.0131 val_acc=0.9947
Epoch 76/100 | train_loss=0.0098 train_acc=0.9989 | val_loss=0.0207 val_acc=0.9933
Epoch 77/100 | train_loss=0.0005 train_acc=1.0000 | val_loss=0.0170 val_acc=0.9973
Epoch 78/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0135 val_acc=0.9960
Epoch 79/100 | train_loss=0.0002 train_acc=1.0000 | val_loss=0.0216 val_acc=0.9920
Epoch 80/100 | train_loss=0.0002 train_acc=1.0000 | val_loss=0.0141 val_acc=0.9973
Epoch 81/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0120 val_acc=0.9960
Epoch 82/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0203 val_acc=0.9920
Epoch 83/100 | train_loss=0.0052 train_acc=0.9983 | val_loss=0.0588 val_acc=0.9840
Epoch 84/100 | train_loss=0.0025 train_acc=0.9994 | val_loss=0.0164 val_acc=0.9947
Epoch 85/100 | train_loss=0.0060 train_acc=0.9980 | val_loss=0.0220 val_acc=0.9907
Epoch 86/100 | train_loss=0.0035 train_acc=0.9994 | val_loss=0.0224 val_acc=0.9947
Epoch 87/100 | train_loss=0.0016 train_acc=0.9994 | val_loss=0.0187 val_acc=0.9920
Epoch 88/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0207 val_acc=0.9907
Epoch 89/100 | train_loss=0.0004 train_acc=1.0000 | val_loss=0.0177 val_acc=0.9947
Epoch 90/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0193 val_acc=0.9907
Epoch 91/100 | train_loss=0.0002 train_acc=1.0000 | val_loss=0.0157 val_acc=0.9947
Epoch 92/100 | train_loss=0.0001 train_acc=1.0000 | val_loss=0.0140 val_acc=0.9947
Epoch 93/100 | train_loss=0.0004 train_acc=0.9997 | val_loss=0.0223 val_acc=0.9920
Epoch 94/100 | train_loss=0.0001 train_acc=1.0000 | val_loss=0.0183 val_acc=0.9933
Epoch 95/100 | train_loss=0.0082 train_acc=0.9991 | val_loss=0.0515 val_acc=0.9880
Epoch 96/100 | train_loss=0.0154 train_acc=0.9957 | val_loss=0.0271 val_acc=0.9933
Epoch 97/100 | train_loss=0.0014 train_acc=0.9997 | val_loss=0.0295 val_acc=0.9933
Epoch 98/100 | train_loss=0.0016 train_acc=0.9997 | val_loss=0.0209 val_acc=0.9933
Epoch 99/100 | train_loss=0.0005 train_acc=1.0000 | val_loss=0.0213 val_acc=0.9947
Epoch 100/100 | train_loss=0.0005 train_acc=0.9997 | val_loss=0.0191 val_acc=0.9947

Evaluating on test set...
Figure(400x400)
Figure(1200x450)

Done. Results saved to: /content/drive/MyDrive/diffusion_project/results/resnet50/results.json
Checkpoint saved to: /content/drive/MyDrive/diffusion_project/results/resnet50/checkpoint.pth

Summary — resnet50:
  Test Accuracy:  0.9960
  Test Precision: 0.9947
  Test Recall:    0.9973
  Test F1:        0.9960
  Parameters:     23,512,130
  Model size:     90.03 MB
  Avg latency:    3.54 ms/image

densenet121:
Using device: cuda
Classes: ['ai', 'nature']

model.safetensors: downloading bytes:  38% 12.1M/32.3M [00:02<00:01, 10.5MB/s,  741kB/s  ]
model.safetensors: downloading bytes:  74% 23.9M/32.3M [00:02<00:00, 25.1MB/s, 1.15MB/s  ]
model.safetensors: reconstructing file:  69% 22.2M/32.3M [00:02<00:01, 9.11MB/s, 1.89MB/s  ]
model.safetensors: reconstructing file:  75% 24.2M/32.3M [00:02<00:00, 9.94MB/s, 2.09MB/s  ]
model.safetensors: reconstructing file:  85% 27.5M/32.3M [00:02<00:00, 11.0MB/s, 2.32MB/s  ]
model.safetensors: reconstructing file:  94% 30.3M/32.3M [00:03<00:00, 11.6MB/s, 2.58MB/s  ]
model.safetensors: downloading bytes: 100% 31.1M/31.1M [00:03<00:00, 9.99MB/s, 2.76MB/s  ]
model.safetensors: reconstructing file: 100% 32.3M/32.3M [00:03<00:00, 10.4MB/s, 2.90MB/s  ]
Epoch 1/100 | train_loss=0.3236 train_acc=0.8551 | val_loss=0.1656 val_acc=0.9307
Epoch 2/100 | train_loss=0.0933 train_acc=0.9686 | val_loss=0.0712 val_acc=0.9680
Epoch 3/100 | train_loss=0.0551 train_acc=0.9791 | val_loss=0.0797 val_acc=0.9640
Epoch 4/100 | train_loss=0.0467 train_acc=0.9843 | val_loss=0.0948 val_acc=0.9653
Epoch 5/100 | train_loss=0.0519 train_acc=0.9811 | val_loss=0.1275 val_acc=0.9493
Epoch 6/100 | train_loss=0.0303 train_acc=0.9891 | val_loss=0.0610 val_acc=0.9733
Epoch 7/100 | train_loss=0.0267 train_acc=0.9900 | val_loss=0.0634 val_acc=0.9747
Epoch 8/100 | train_loss=0.0193 train_acc=0.9931 | val_loss=0.0791 val_acc=0.9760
Epoch 9/100 | train_loss=0.0285 train_acc=0.9897 | val_loss=0.0664 val_acc=0.9800
Epoch 10/100 | train_loss=0.0198 train_acc=0.9929 | val_loss=0.0641 val_acc=0.9827
Epoch 11/100 | train_loss=0.0207 train_acc=0.9929 | val_loss=0.0495 val_acc=0.9813
Epoch 12/100 | train_loss=0.0113 train_acc=0.9969 | val_loss=0.0470 val_acc=0.9853
Epoch 13/100 | train_loss=0.0261 train_acc=0.9900 | val_loss=0.1006 val_acc=0.9680
Epoch 14/100 | train_loss=0.0122 train_acc=0.9971 | val_loss=0.0364 val_acc=0.9880
Epoch 15/100 | train_loss=0.0108 train_acc=0.9960 | val_loss=0.0372 val_acc=0.9840
Epoch 16/100 | train_loss=0.0276 train_acc=0.9891 | val_loss=0.0766 val_acc=0.9760
Epoch 17/100 | train_loss=0.0111 train_acc=0.9974 | val_loss=0.0474 val_acc=0.9840
Epoch 18/100 | train_loss=0.0107 train_acc=0.9971 | val_loss=0.0373 val_acc=0.9813
Epoch 19/100 | train_loss=0.0057 train_acc=0.9980 | val_loss=0.0451 val_acc=0.9853
Epoch 20/100 | train_loss=0.0032 train_acc=0.9997 | val_loss=0.0241 val_acc=0.9933
Epoch 21/100 | train_loss=0.0025 train_acc=0.9997 | val_loss=0.0432 val_acc=0.9827
Epoch 22/100 | train_loss=0.0065 train_acc=0.9974 | val_loss=0.0444 val_acc=0.9840
Epoch 23/100 | train_loss=0.0383 train_acc=0.9854 | val_loss=0.1396 val_acc=0.9627
Epoch 24/100 | train_loss=0.0230 train_acc=0.9914 | val_loss=0.0894 val_acc=0.9720
Epoch 25/100 | train_loss=0.0076 train_acc=0.9974 | val_loss=0.0708 val_acc=0.9760
Epoch 26/100 | train_loss=0.0131 train_acc=0.9957 | val_loss=0.0604 val_acc=0.9827
Epoch 27/100 | train_loss=0.0118 train_acc=0.9963 | val_loss=0.1577 val_acc=0.9613
Epoch 28/100 | train_loss=0.0050 train_acc=0.9986 | val_loss=0.0546 val_acc=0.9853
Epoch 29/100 | train_loss=0.0032 train_acc=0.9989 | val_loss=0.0552 val_acc=0.9853
Epoch 30/100 | train_loss=0.0082 train_acc=0.9974 | val_loss=0.0422 val_acc=0.9827
Epoch 31/100 | train_loss=0.0083 train_acc=0.9980 | val_loss=0.0312 val_acc=0.9867
Epoch 32/100 | train_loss=0.0612 train_acc=0.9817 | val_loss=0.1387 val_acc=0.9600
Epoch 33/100 | train_loss=0.0144 train_acc=0.9946 | val_loss=0.0434 val_acc=0.9880
Epoch 34/100 | train_loss=0.0062 train_acc=0.9983 | val_loss=0.0473 val_acc=0.9880
Epoch 35/100 | train_loss=0.0059 train_acc=0.9977 | val_loss=0.0378 val_acc=0.9880
Epoch 36/100 | train_loss=0.0049 train_acc=0.9983 | val_loss=0.0476 val_acc=0.9853
Epoch 37/100 | train_loss=0.0123 train_acc=0.9963 | val_loss=0.0872 val_acc=0.9787
Epoch 38/100 | train_loss=0.0094 train_acc=0.9966 | val_loss=0.0660 val_acc=0.9787
Epoch 39/100 | train_loss=0.0057 train_acc=0.9971 | val_loss=0.0449 val_acc=0.9840
Epoch 40/100 | train_loss=0.0063 train_acc=0.9969 | val_loss=0.0516 val_acc=0.9760
Epoch 41/100 | train_loss=0.0038 train_acc=0.9991 | val_loss=0.0528 val_acc=0.9800
Epoch 42/100 | train_loss=0.0173 train_acc=0.9954 | val_loss=0.0602 val_acc=0.9813
Epoch 43/100 | train_loss=0.0642 train_acc=0.9789 | val_loss=0.0507 val_acc=0.9827
Epoch 44/100 | train_loss=0.0071 train_acc=0.9980 | val_loss=0.0379 val_acc=0.9893
Epoch 45/100 | train_loss=0.0094 train_acc=0.9963 | val_loss=0.0302 val_acc=0.9893
Epoch 46/100 | train_loss=0.0077 train_acc=0.9969 | val_loss=0.0276 val_acc=0.9893
Epoch 47/100 | train_loss=0.0044 train_acc=0.9991 | val_loss=0.0232 val_acc=0.9920
Epoch 48/100 | train_loss=0.0065 train_acc=0.9969 | val_loss=0.0345 val_acc=0.9933
Epoch 49/100 | train_loss=0.0015 train_acc=0.9997 | val_loss=0.0355 val_acc=0.9867
Epoch 50/100 | train_loss=0.0015 train_acc=0.9994 | val_loss=0.0319 val_acc=0.9880
Epoch 51/100 | train_loss=0.0018 train_acc=0.9997 | val_loss=0.0368 val_acc=0.9880
Epoch 52/100 | train_loss=0.0018 train_acc=0.9997 | val_loss=0.0230 val_acc=0.9920
Epoch 53/100 | train_loss=0.0009 train_acc=1.0000 | val_loss=0.0233 val_acc=0.9893
Epoch 54/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0196 val_acc=0.9933
Epoch 55/100 | train_loss=0.0026 train_acc=0.9991 | val_loss=0.0287 val_acc=0.9893
Epoch 56/100 | train_loss=0.0201 train_acc=0.9940 | val_loss=0.0436 val_acc=0.9893
Epoch 57/100 | train_loss=0.0110 train_acc=0.9957 | val_loss=0.0321 val_acc=0.9880
Epoch 58/100 | train_loss=0.0244 train_acc=0.9909 | val_loss=0.0368 val_acc=0.9880
Epoch 59/100 | train_loss=0.0070 train_acc=0.9974 | val_loss=0.0158 val_acc=0.9907
Epoch 60/100 | train_loss=0.0019 train_acc=1.0000 | val_loss=0.0139 val_acc=0.9960
Epoch 61/100 | train_loss=0.0074 train_acc=0.9977 | val_loss=0.0354 val_acc=0.9827
Epoch 62/100 | train_loss=0.0189 train_acc=0.9949 | val_loss=0.0434 val_acc=0.9907
Epoch 63/100 | train_loss=0.0039 train_acc=0.9991 | val_loss=0.0290 val_acc=0.9907
Epoch 64/100 | train_loss=0.0078 train_acc=0.9977 | val_loss=0.1713 val_acc=0.9547
Epoch 65/100 | train_loss=0.0090 train_acc=0.9969 | val_loss=0.0213 val_acc=0.9933
Epoch 66/100 | train_loss=0.0114 train_acc=0.9966 | val_loss=0.0331 val_acc=0.9880
Epoch 67/100 | train_loss=0.0025 train_acc=0.9994 | val_loss=0.0223 val_acc=0.9920
Epoch 68/100 | train_loss=0.0212 train_acc=0.9931 | val_loss=0.0536 val_acc=0.9853
Epoch 69/100 | train_loss=0.0066 train_acc=0.9980 | val_loss=0.0551 val_acc=0.9840
Epoch 70/100 | train_loss=0.0068 train_acc=0.9983 | val_loss=0.0484 val_acc=0.9840
Epoch 71/100 | train_loss=0.0038 train_acc=0.9986 | val_loss=0.0308 val_acc=0.9907
Epoch 72/100 | train_loss=0.0031 train_acc=0.9991 | val_loss=0.0180 val_acc=0.9933
Epoch 73/100 | train_loss=0.0005 train_acc=1.0000 | val_loss=0.0276 val_acc=0.9907
Epoch 74/100 | train_loss=0.0004 train_acc=1.0000 | val_loss=0.0195 val_acc=0.9933
Epoch 75/100 | train_loss=0.0002 train_acc=1.0000 | val_loss=0.0246 val_acc=0.9920
Epoch 76/100 | train_loss=0.0007 train_acc=0.9997 | val_loss=0.0302 val_acc=0.9933
Epoch 77/100 | train_loss=0.0002 train_acc=1.0000 | val_loss=0.0287 val_acc=0.9933
Epoch 78/100 | train_loss=0.0008 train_acc=0.9997 | val_loss=0.0361 val_acc=0.9920
Epoch 79/100 | train_loss=0.0053 train_acc=0.9977 | val_loss=0.0480 val_acc=0.9893
Epoch 80/100 | train_loss=0.0052 train_acc=0.9989 | val_loss=0.0991 val_acc=0.9760
Epoch 81/100 | train_loss=0.0100 train_acc=0.9971 | val_loss=0.0285 val_acc=0.9853
Epoch 82/100 | train_loss=0.0227 train_acc=0.9923 | val_loss=0.0337 val_acc=0.9893
Epoch 83/100 | train_loss=0.0226 train_acc=0.9931 | val_loss=0.0332 val_acc=0.9880
Epoch 84/100 | train_loss=0.0060 train_acc=0.9989 | val_loss=0.0371 val_acc=0.9920
Epoch 85/100 | train_loss=0.0035 train_acc=0.9997 | val_loss=0.0404 val_acc=0.9907
Epoch 86/100 | train_loss=0.0009 train_acc=0.9997 | val_loss=0.0428 val_acc=0.9920
Epoch 87/100 | train_loss=0.0005 train_acc=1.0000 | val_loss=0.0344 val_acc=0.9920
Epoch 88/100 | train_loss=0.0004 train_acc=1.0000 | val_loss=0.0313 val_acc=0.9920
Epoch 89/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0313 val_acc=0.9920
Epoch 90/100 | train_loss=0.0002 train_acc=1.0000 | val_loss=0.0364 val_acc=0.9920
Epoch 91/100 | train_loss=0.0005 train_acc=1.0000 | val_loss=0.0420 val_acc=0.9907
Epoch 92/100 | train_loss=0.0008 train_acc=0.9997 | val_loss=0.0674 val_acc=0.9867
Epoch 93/100 | train_loss=0.0002 train_acc=1.0000 | val_loss=0.0481 val_acc=0.9907
Epoch 94/100 | train_loss=0.0003 train_acc=1.0000 | val_loss=0.0476 val_acc=0.9920
Epoch 95/100 | train_loss=0.0013 train_acc=0.9991 | val_loss=0.0548 val_acc=0.9880
Epoch 96/100 | train_loss=0.0166 train_acc=0.9943 | val_loss=0.1786 val_acc=0.9653
Epoch 97/100 | train_loss=0.0176 train_acc=0.9934 | val_loss=0.0950 val_acc=0.9760
Epoch 98/100 | train_loss=0.0118 train_acc=0.9949 | val_loss=0.0337 val_acc=0.9880
Epoch 99/100 | train_loss=0.0097 train_acc=0.9974 | val_loss=0.0388 val_acc=0.9867
Epoch 100/100 | train_loss=0.0109 train_acc=0.9963 | val_loss=0.0393 val_acc=0.9907

Evaluating on test set...
Figure(400x400)
Figure(1200x450)

Done. Results saved to: /content/drive/MyDrive/diffusion_project/results/densenet121/results.json
Checkpoint saved to: /content/drive/MyDrive/diffusion_project/results/densenet121/checkpoint.pth

Summary — densenet121:
  Test Accuracy:  0.9960
  Test Precision: 1.0000
  Test Recall:    0.9920
  Test F1:        0.9960
  Parameters:     6,955,906
  Model size:     27.31 MB
  Avg latency:    2.90 ms/image
