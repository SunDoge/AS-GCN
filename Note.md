# Note

## 把ST-GCN的data软连接到这里

```bash
export STGCN=/home/dataset/st-gcn/data

ln -s $STGCN/NTU-RGB-D/xsub/train_data.npy ./data/nturgb_d/xsub/train_data_joint_pad.npy
ln -s $STGCN/NTU-RGB-D/xsub/train_label.pkl ./data/nturgb_d/xsub/train_label.pkl

ln -s $STGCN/NTU-RGB-D/xsub/val_data.npy ./data/nturgb_d/xsub/val_data_joint_pad.npy
ln -s $STGCN/NTU-RGB-D/xsub/val_label.pkl ./data/nturgb_d/xsub/val_label.pkl
```