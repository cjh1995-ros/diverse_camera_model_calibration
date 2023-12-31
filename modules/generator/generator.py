from modules import conv_pose2transform, conv_transform2pose
from modules.generator import BasicGenerator
from modules.cameras import Camera
from typing import Dict, List
import json
# import numpy as np
from autograd import numpy as np




class CameraGenerator(BasicGenerator):
    def generate(self, datas: List[Dict]):
        cameras = []
        
        for i, data in enumerate(datas):
            tmp = Camera(data['id'],
                         data['intr_opt_type'],
                         data['is_extr_opt'],
                         data['proj_func_type'],
                         data['dist_type'])
            
            tmp.initial_params = data['init_params']
            
            cameras.append(tmp)
            
        return cameras                
    
    def generate_from_file(self, file_path: str):
        with open(file_path, 'r') as f:
            datas = json.load(f)
            
        return self.generate(datas)
    

    def generate_default(self):
        from scipy.spatial.transform import Rotation as R
        datas = []
        
        ori1 = np.array([[1, 0, 0], 
                         [0, 0, 1], 
                         [0, -1, 0]], dtype=np.float32)
        
        rot1 = np.array([0, np.pi/6, 0], dtype=np.float32)
        ori1 = ori1 @ R.from_rotvec(rot1).as_matrix()
        
        ori_rvec1 = R.from_matrix(ori1).as_rotvec()
        pos1 = np.array([-2.0, -3.0, 1.0], dtype=np.float32)
        pose1 = np.concatenate([ori_rvec1, pos1])
        transform1 = conv_pose2transform(pose1)
        
        ori2 = np.array([[1, 0, 0], 
                         [0, 0, 1], 
                         [0, -1, 0]], dtype=np.float32)

        rot2 = np.array([0, -np.pi/6, 0], dtype=np.float32)
        ori2 = ori2 @ R.from_rotvec(rot2).as_matrix()

        ori_rvec2 = R.from_matrix(ori2).as_rotvec()
        pos2 = np.array([4.0, -2.5, 1.0], dtype=np.float32)
        pose2 = np.concatenate([ori_rvec2, pos2])
        transform2 = conv_pose2transform(pose2)
        
        ori3 = np.array([[1, 0, 0], 
                         [0, 0, 1], 
                         [0, -1, 0]], dtype=np.float32)

        rot3 = np.array([0, -np.pi * 2/3, -np.pi/3], dtype=np.float32)
        ori3 = ori3 @ R.from_rotvec(rot3).as_matrix()

        ori_rvec3 = R.from_matrix(ori3).as_rotvec()
        pos3 = np.array([5.0, 5.0, 5.0], dtype=np.float32)
        pose3 = np.concatenate([ori_rvec3, pos3])
        transform3 = conv_pose2transform(pose3)

        ori4 = np.array([[1, 0, 0], 
                         [0, 0, 1], 
                         [0, -1, 0]], dtype=np.float32)
        pos4 = np.array([-2.0, 5.0, 6.0], dtype=np.float32) # 

        rot4 = np.array([0, np.pi * 2/3, np.pi/3], dtype=np.float32)
        ori4 = ori4 @ R.from_rotvec(rot4).as_matrix()

        ori_rvec4 = R.from_matrix(ori4).as_rotvec()
        pose4 = np.concatenate([ori_rvec4, pos4])
        transform4 = conv_pose2transform(pose4)
        
        datas.append({"id": 0, 
                      "intr_opt_type": "FOCAL", 
                      "is_extr_opt": True, 
                      "proj_func_type": "PERSPECTIVE", 
                      "dist_type": "POLYNOMIAL",
                      "init_params": [1000.0, 500.0, 500.0, -0.2, 0.1, transform1[0], transform1[1], transform1[2], transform1[3], transform1[4], transform1[5]]})

        datas.append({"id": 1, 
                      "intr_opt_type": "FOCAL", 
                      "is_extr_opt": True, 
                      "proj_func_type": "PERSPECTIVE", 
                      "dist_type": "POLYNOMIAL",
                      "init_params": [1000.0, 500.0, 500.0, -0.2, 0.1, transform2[0], transform2[1], transform2[2], transform2[3], transform2[4], transform2[5]]})

        datas.append({"id": 2, 
                      "intr_opt_type": "FOCAL", 
                      "is_extr_opt": True, 
                      "proj_func_type": "PERSPECTIVE", 
                      "dist_type": "POLYNOMIAL",
                      "init_params": [1000.0, 500.0, 500.0, -0.2, 0.1, transform3[0], transform3[1], transform3[2], transform3[3], transform3[4], transform3[5]]})

        datas.append({"id": 3, 
                      "intr_opt_type": "FOCAL", 
                      "is_extr_opt": True, 
                      "proj_func_type": "PERSPECTIVE", 
                      "dist_type": "POLYNOMIAL",
                      "init_params": [1000.0, 500.0, 500.0, -0.2, 0.1, transform4[0], transform4[1], transform4[2], transform4[3], transform4[4], transform4[5]]})
                
        return self.generate(datas)
    
    
from modules.markers.point import Feature3D
from modules.markers.rectangle import Rect3D

class MarkerGenerator(BasicGenerator):
    def generate(self, datas: List[Dict]):
        """"""
            
    def generate_from_file(self, file_path: str):
        """"""    

    def generate_default(self):
        """"""
        first = np.array([[0.0, 0.0, 0.0],
                          [0.0, 1.0, 0.0],
                          [1.0, 1.0, 0.0],
                          [1.0, 0.0, 0.0]], dtype=np.float32)
        
        second = np.array([[1.5, 1.0, 0.0],
                           [2.5, 1.0, 0.0],
                           [2.5, 2.0, 0.0],
                           [1.5, 2.0, 0.0]], dtype=np.float32)
        
        third = np.array([[0.5, 3.0, 1.0],
                          [1.5, 3.0, 1.0],
                          [1.5, 4.0, 2.0],
                          [0.5, 4.0, 2.0]], dtype=np.float32)
        
        fourth = np.array([[2.0, 3.5, 1.5],
                            [3.0, 3.5, 1.5],
                            [3.0, 4.5, 2.5],
                            [2.0, 4.5, 2.5]], dtype=np.float32)
        
        hinz = np.array([0.0, 2.0, 0.0], dtype=np.float32)
        
        return [first, second, third, fourth], hinz
        
    def generate_from_array(self, datas: np.ndarray):
        """"""
        feature_container = []
        
        for i, pt in enumerate(datas):
            tmp = Feature3D(pt[0], pt[1], pt[2])
            tmp.id = i
            
            feature_container.append(tmp)
            
        return feature_container
        
class RectangleGenerator(BasicGenerator):
    def generate(self, datas: List[Dict]):
        """"""