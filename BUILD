load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")

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
        requirement("werkzeug"),
        requirement("jinja2"),
        requirement("click"),
        requirement("itsdangerous"),
    ]
)

py3_image(
    name = "image",
    srcs = ["src/app.py"],
    deps = [
        requirement("Flask"),
        requirement("werkzeug"),
        requirement("jinja2"),
        requirement("click"),
        requirement("itsdangerous"),
    ],
    main = "src/app.py"
)
