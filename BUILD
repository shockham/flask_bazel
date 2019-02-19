load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")

load(
  "@io_bazel_rules_python//python:python.bzl",
  "py_binary", "py_library", "py_test",
)

load("@deps//:requirements.bzl", "requirement")

py_library(
    name = "app_lib",
    srcs = ["src/app.py"],
    deps = [
        requirement("Flask"),
        requirement("werkzeug"),
        requirement("jinja2"),
        requirement("click"),
        requirement("itsdangerous"),
    ]
)

py_binary(
    name = "app",
    srcs = ["run.py"],
    deps = [
        ":app_lib",
    ],
    main = "run.py"
)

py_test(
    name = "test",
    srcs = [
        "tests/test_main.py",
    ],
    deps = [
        ":app_lib"
    ],
    main = "test_main.py"
)

py3_image(
    name = "image",
    srcs = [ "run.py" ],
    deps = [
        ":app_lib"
    ],
    main = "run.py"
)
