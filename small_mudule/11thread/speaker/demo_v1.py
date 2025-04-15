'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2025-04-16 00:24:35
LastEditTime: 2025-04-16 00:24:39
FilePath: /python-libraries/small_mudule/11thread/demo1.py
'''
import time
import threading
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError

class VoiceSemanticListener:
    def __init__(self):
        self.recognizer = Recognizer()
        self.microphone = Microphone()
        self.is_listening = False
        self.callbacks = {
            "开始": [],
            "结束": []
        }

        # 校准环境噪音
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

    def register_callback(self, keyword, callback):
        """注册关键词回调函数"""
        if keyword in self.callbacks:
            self.callbacks[keyword].append(callback)
        else:
            print(f"警告: 不支持的关键词 {keyword}")

    def _listen_loop(self):
        """后台监听循环"""
        with self.microphone as source:
            while self.is_listening:
                try:
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=2)
                    text = self.recognizer.recognize_google(audio, language='zh-CN')
                    print(f"识别结果: {text}")

                    # 语义匹配
                    for keyword in self.callbacks:
                        if keyword in text:
                            for callback in self.callbacks[keyword]:
                                callback()

                except UnknownValueError:
                    pass  # 无有效语音输入
                except RequestError as e:
                    print(f"语音识别服务错误: {e}")
                except Exception as e:
                    print(f"未知错误: {e}")

    def start(self):
        """开始监听"""
        if not self.is_listening:
            self.is_listening = True
            self.thread = threading.Thread(target=self._listen_loop)
            self.thread.start()
            print("语音监听已启动")

    def stop(self):
        """停止监听"""
        if self.is_listening:
            self.is_listening = False
            self.thread.join()
            print("语音监听已停止")

# 使用示例 ==============================================
if __name__ == "__main__":
    def on_start():
        print("检测到「开始」指令 → 执行启动操作")

    def on_end():
        print("检测到「结束」指令 → 执行终止操作")

    # 初始化监听器
    listener = VoiceSemanticListener()
    
    # 注册语义回调
    listener.register_callback("开始", on_start)
    listener.register_callback("结束", on_end)

    # 开始监听
    listener.start()

    # 保持主线程运行（实际使用时可以结合其他逻辑）
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        listener.stop()