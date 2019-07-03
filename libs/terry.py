from flask import Flask, render_template, request, json, Response, jsonify
import jieba
import sqlite3
import csv
import Terry_toolkit as tkit
import libs
from random import choice
import random
import os,json
class Terry:

  # def c_inputfile(self,inputfile,data):
  #     """创建预测文件

  #     """
  #     with open(inputfile,"ab+") as f:
  #         json.dump(data,f)
  #         print("创建训练资料完成..."+inputfile)
  #         return True

    def c_inputfile(self,inputfile,data):
      """创建预测文件

      """
      # str = json.dumps(data)

      # print(str)
      # print(type(str))
      # with open(inputfile,"ab+") as f:
      #   f.write(str)  
      # print("创建训练资料完成..."+inputfile)
      # return True
      # json_str = json.dumps(data)
      with open(inputfile, 'a') as outfile:
          # json_file.write('json_str')
          json.dump(data, outfile)
          outfile.write('\n')