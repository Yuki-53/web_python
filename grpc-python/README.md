gRPC server can return song based on input genre

To compile protobuf files run 
```
python -m grpc_tools.protoc -I definitions/ --python_out=definitions/builds/ \
--grpc_python_out=definitions/builds/ definitions/service.proto
```

To run server `python server.py`

To run client `python client.py`

To run tests `python -m unittest discover -p "tests*"`
