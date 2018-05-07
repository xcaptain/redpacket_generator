from flask import Flask, json
from flask import request
from redpacket_policy import RedpacketPolicy

app = Flask(__name__)

# 获取统计报表
@app.route("/")
def gen():
    amount = int(request.args.get('amount', 100)) # 至少1元钱，100分
    total = int(request.args.get('total', 1)) # 至少分1份

    policy = RedpacketPolicy()
    sample = policy.gen(amount, total)
    data = {'sample': sample}
    return json.dumps(data)
