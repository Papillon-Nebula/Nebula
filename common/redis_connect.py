# import redis

# # 指定 Redis服务器的 IP 地址， 端口号 和 数据库进行连接
# # red = redis.Redis(host='127.0.0.1', port=6379, db=0)

# pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True, db=0)
# red = redis.Redis(connection_pool=pool)