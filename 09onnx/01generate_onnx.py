'''
Description:  构造onnx模型 https://www.yuque.com/huangzhongqing/pytorch/ucvem31c9nimql9m#M2KTQ
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-13 18:20:59
LastEditTime: 2023-12-13 18:24:45
FilePath: /python-libraries/09onnx/01generate_onnx.py
'''
import onnx 
from onnx import helper 
from onnx import TensorProto 
 
# input and output 
a = helper.make_tensor_value_info('a', TensorProto.FLOAT, [10, 10]) 
x = helper.make_tensor_value_info('x', TensorProto.FLOAT, [10, 10]) 
b = helper.make_tensor_value_info('b', TensorProto.FLOAT, [10, 10]) 
output = helper.make_tensor_value_info('output', TensorProto.FLOAT, [10, 10]) 
 
# Mul 
mul = helper.make_node('Mul', ['a', 'x'], ['c']) 
 
# Add 
add = helper.make_node('Add', ['c', 'b'], ['output']) 
 
# graph and model 
graph = helper.make_graph([mul, add], 'linear_func', [a, x, b], [output]) 
model = helper.make_model(graph) 
 
# save model 
onnx.checker.check_model(model) 
print(model) 
onnx.save(model, 'linear_func.onnx')

'''  
ir_version: 8
graph {
  node {
    input: "a"
    input: "x"
    output: "c"
    op_type: "Mul"
  }
  node {
    input: "c"
    input: "b"
    output: "output"
    op_type: "Add"
  }
  name: "linear_func"
  input {
    name: "a"
    type {
      tensor_type {
        elem_type: 1
        shape {
          dim {
            dim_value: 10
          }
          dim {
            dim_value: 10
          }
        }
      }
    }
  }
  input {
    name: "x"
    type {
      tensor_type {
        elem_type: 1
        shape {
          dim {
            dim_value: 10
          }
          dim {
            dim_value: 10
          }
        }
      }
    }
  }
  input {
    name: "b"
    type {
      tensor_type {
        elem_type: 1
        shape {
          dim {
            dim_value: 10
          }
          dim {
            dim_value: 10
          }
        }
      }
    }
  }
  output {
    name: "output"
    type {
      tensor_type {
        elem_type: 1
        shape {
          dim {
            dim_value: 10
          }
          dim {
            dim_value: 10
          }
        }
      }
    }
  }
}
opset_import {
  version: 17
}
'''