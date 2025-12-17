from abc import ABC, abstractmethod

class AI_Model(ABC):
    def load_data(self,data):
        print("ĐANG NẠP DỮ LIỆU")
    @abstractmethod
    def predict(self, input_data):
        pass

class Chatbot(AI_Model):
    def predict(self, input_data):
        return f"Chatbot đang trả lời: {input_data}"
class FaceRec(AI_Model):
    def predict(self, input_data):
        return f"Đang Quét khuôn mặt trong ảnh... Phát hiện : Dony."
    
models = [Chatbot(),FaceRec(),Chatbot()]

for model in models:
    print(model.predict("TEST DATA"))
