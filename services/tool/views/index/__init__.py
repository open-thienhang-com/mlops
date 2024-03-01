from flask_restx import Namespace, Resource
from flask import Flask, render_template,jsonify,request

ns_model = Namespace(
    "/a",
    description="Test V1")


@ns_model.route("")
@ns_model.doc(
    responses={
        200: "Success",
        400: "Bad request",
    },
)
class NamespaceTestV1(Resource):
    def get(self):
        """Flask namespace"""
        try:
            return render_template('index.html')
        except Exception as err:
            print(err)
            return 400
