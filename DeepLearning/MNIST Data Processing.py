#VERİ YÜKLEME
import torch

from torchvision import datasets, transforms

#torchvision =Görsel veri kütüphanesi
#ToTensor =28x28 resim -> 28x28 sayı matrisi

transform=transforms.ToTensor()
#piksel -> sayı dizisi
train_dataset = datasets.MNIST(root="data", train=True, transform=transform, download=True)
#data1\ isimli klasörde eğitim verisini kaydet
test_dataset = datasets.MNIST(root="data", train=False, transform=transform, download=True)

from torch.utils.data import DataLoader
#Veriyi küçük parçalara ayırma
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True) #60.000 resim
# shuffle = veriyi karıştır
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False) #10.000 resim
# Batch içeriği: images= shape:[32,1,28,28] (32 resim,1 kanal, 28x28 piksel) labels= shape[32] (0-9 arası çıktı)

#MODEL TANIMLAMA
# 28x28=784 sayı -> (-1,784)

import torch.nn as nn
model = nn.Sequential(
    nn.Flatten(), #[32, 1, 28, 28] -> [32,784]
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Linear(64, 10),
)
#güven skorunu üretimi

#LOSS ve OPTIMIZER(Ağırlık Değişimi) EKLEME

#loss.backward() "hangi ağırlık ne kadar hatalı" hesaplar (gradyan)
#optimizer.step() ağırlıkları o gradyana göre günceller

import torch.optim as optim

criterion = nn.CrossEntropyLoss()  #Loss hesaplama,loss yüksekse cezalandırır (ceze:Ağırlık yüksek değişim gösterir)
optimizer = optim.Adam(model.parameters(), lr=0.001) #ADAM Optimizer ekleme #Öğreneme hızı=ağırlıkların değişim ölçütü

#EĞİTİM DÖNGÜSÜ

train_losses = [] #Öğrenme kayıpları
test_accuracies = [] #Test doğrulukları

for epoch in range(5): #Veriyi tanıtma
    model.train()
    toplam_loss = 0
    for images, labels in train_loader:  # images= [32, 1, 28, 28] labels= gerçek değerler ( 60.000 resim ÷ 32 = 1875 kez )
        optimizer.zero_grad()  # Önceki gradyanları sıfırla(for döngüsü sebebiyle) her batch(32 resim) başında temizlemek gerekli birikmemesi için
        cikti = model(images)  # her image modelden geçerek her biri 10 çıktı değeri oluşturuyor
        loss = criterion(cikti, labels)  # çıktı gerçek etiketle karşılaştırılır ve loss hesaplanır
        loss.backward()  # lossa göre her ağırlığa bir gradyan değeri atıyor:
        optimizer.step()  # gradyanları kullanarak ağırlıkları güncelliyor
        toplam_loss += loss.item()  # O batch'in loss değerini epoch toplamına ekliyor.
    epoch_loss = toplam_loss / len(train_loader)  # 1875 batch bittikten sonra bu toplamı 1875'e bölerek epoch'un ortalama lossunu buluyorsun.
    train_losses.append(epoch_loss)

    # TEST DEĞERLENDİRMESİ  NOT: hala epoch döngüsü içindeyiz

    model.eval() #ağırlık değişimi ve gradyan hesabı olmayacak sadece bakılacak
    dogru = 0
    toplam = 0
    with torch.no_grad(): #gradyan takibini kapat demek
        for images, labels in test_loader: #
            cikti = model(images) # 32 test resmi modelden geçiyor, 32×10'luk skor tablosu çıkıyor
            tahmin = cikti.argmax(dim=1) # Her resim için 10 skorun en büyüğünün indeksini alıyor:
            dogru += (tahmin == labels).sum().item() # Tahmini gerçek etiketle karşılaştırıp kaç doğru çıktı bilgisini tutuyor
            toplam += labels.size(0) # 10.000, 32 ye tam bölünmez bu yüzden son batch daha az olabilir. Toplam resim sayısını takip ediyor.

    accuracy = dogru / toplam  #doğruluk oranı hesabı
    test_accuracies.append(accuracy)

    print(f"Epoch {epoch+1} | Loss: {epoch_loss:.4f} | Doğruluk_Oranı: {accuracy:.4f}")

#GRAFİK ADD

import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4)) #fig = tüm alan temsil eder.1 satır 2 sutun bir grafik olacak , Genişliği 10 birim, Yüksekliği 4 birim

ax1.plot(train_losses, marker='o', color='red') #train_losses listeni çizgi grafik olarak çiziyor
ax1.set_title("Eğitim Loss") #grafik başlığı
ax1.set_xlabel("Epoch") #X ekseni otomatik olarak epoch numarası oluyor
ax1.set_ylabel("Loss") #Y ekseni loss değerleri.

ax2.plot(test_accuracies, marker='o', color='green')
ax2.set_title("Test Accuracy")
ax2.set_xlabel("Epoch")
ax2.set_ylabel("Accuracy")

plt.tight_layout() #iki grafiği düzenli tutuyor
plt.show() #grafiği göster