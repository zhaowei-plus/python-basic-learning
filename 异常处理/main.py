
## 异常的捕获
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ 不能除以零！")
finally:
    print("异常捕获案例！")


### 自定义HTTP 异常类

# 基础 HTTP 异常类
class HTTPException(Exception):
    """所有自定义 HTTP 异常的基类"""
    def __init__(self, message="HTTP 请求发生错误"):
        self.message = message
        super().__init__(self.message)


# 请求参数错误
class BadRequestException(HTTPException):
    """400 Bad Request"""
    def __init__(self, message="请求参数错误"):
        super().__init__(message)

# 未授权访问（401）
class UnauthorizedException(HTTPException):
    """401 Unauthorized"""
    def __init__(self, message="未授权访问（401）"):
        super().__init__(message)

# 禁止访问（403）
class ForbiddenException(HTTPException):
    """403  Forbidden"""
    def __init__(self, message="禁止访问（403）"):
        super().__init__(message)

# 资源不存在（404）
class NotFoundException(HTTPException):
    """404 Not Found"""
    def __init__(self, message="资源未找到（404）"):
        super().__init__(message)

# 服务器错误
class ServerException(HTTPException):
    """500 Internal Server Error"""
    def __init__(self, message="服务器内部错误（500）"):
        super().__init__(message)

# 请求超时
class TimeoutException(HTTPException):
    """请求超时"""
    def __init__(self, message="请求超时"):
        super().__init__(message)

# 网络连接错误
class NetworkException(HTTPException):
    """网络连接错误"""
    def __init__(self, message="网络连接错误"):
        super().__init__(message)

## 根据状态码返回不同的异常
def handle_http_response(status_code):
    if status_code == 400:
        raise BadRequestException()
    elif status_code == 401:
        raise UnauthorizedException()
    elif status_code == 403:
        raise ForbiddenException()
    elif status_code == 404:
        raise NotFoundException()
    elif status_code == 500:
        raise ServerException()
    else:
        print(f"✅ 请求成功，状态码：{status_code}")

# 测试
try:
    handle_http_response(404)
except NotFoundException as e:
    print(f"捕获到异常：{e}")  # 捕获 404
except HTTPException as e:
    print(f"捕获到其它 HTTP 错误：{e}")