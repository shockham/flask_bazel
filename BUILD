load(
  "@io_bazel_rules_python//python:python.bzl",
  "py_binary", "py_library", "py_test",
)

load("@deps//:requirements.bzl", "requirement")

py_binary(
    name = "app",
    srcs = ["src/app.py"],
    deps = [
        requirement("Flask"),
    ]
)
