_base_ = [
    '../_base_/models/fast_scnn.py', '../_base_/datasets/pascal_escroom.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_160k.py'
]

# Re-config the data sampler.
data = dict(samples_per_gpu=2, workers_per_gpu=4)

# Re-config the optimizer.
optimizer = dict(type='SGD', lr=0.12, momentum=0.9, weight_decay=4e-5)

# runtime settings
checkpoint_config = dict(by_epoch=False, interval=8000)
evaluation = dict(interval=8000, metric='mIoU')