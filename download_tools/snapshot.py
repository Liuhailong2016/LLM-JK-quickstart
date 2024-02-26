from huggingface_hub import snapshot_download
snapshot_download(
  repo_id="mozilla-foundation/common_voice_11_0",
  repo_type="dataset",
  force_download=True,
  resume_download=True,
  local_dir="/home/rr-ai/huggingface_datasets/common_voice_11_0",
  local_dir_use_symlinks=False,
  proxies={"https": "http://192.168.70.165:1081"},
  allow_patterns=[
                  #"*.py","*.json","*.md", 
                  "audio/zh-CN/train/zh-CN_train_*.tar",
                  "audio/zh-CN/test/zh-CN_test_0.tar", 
                  #"audio/zh-CN/dev/zh-CN_dev_0.tar",
                  #"audio/zh-CN/other/*.*",
                  #"audio/zh-CN/invalidated/*.*",
                  #"transcript/zh-CN/*.*"
                  ],
  max_workers=8
)

