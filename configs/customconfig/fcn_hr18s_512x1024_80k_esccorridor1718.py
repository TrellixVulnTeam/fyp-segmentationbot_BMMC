"""
Dataset: ESC Corridor 1718 (VOC Type)
Method: FCN (hrnet)
Backbone:hr18s (We load the hr18 config and make modifications to it)- s stands for small
Crop Size: 512x1024
Lr Schd: 80000
"""

_base_ = [
    '../_base_/models/fcn_hr18.py', '../_base_/datasets/pascal_esccorridor_1718.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]

model = dict(
    pretrained='open-mmlab://msra/hrnetv2_w18_small',
    backbone=dict(
        extra=dict(
            stage1=dict(num_blocks=(2, )),
            stage2=dict(num_blocks=(2, 2)),
            stage3=dict(num_modules=3, num_blocks=(2, 2, 2)),
            stage4=dict(num_modules=2, num_blocks=(2, 2, 2, 2)))),
    decode_head=dict(num_classes=2))