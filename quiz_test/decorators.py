from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        parentid = args[0].request.data.get("parentid", "")
        qid = args[0].request.data.get("qid", "")
        question = args[0].request.data.get("question", "")
        a= args[0].request.data.get("a", "")
        b= args[0].request.data.get("b", "")
        c= args[0].request.data.get("c", "")
        d= args[0].request.data.get("d", "")
        answer = args[0].request.data.get("answer", "")
        importance = args[0].request.data.get("importance", "")
        complexity = args[0].request.data.get("complexity", "")
        time = args[0].request.data.get("time", "")
        marks = args[0].request.data.get("marks", "")
        foundation = args[0].request.data.get("foundation", "")
        subject = args[0].request.data.get("subject", "")
        core = args[0].request.data.get("core", "")
        exam = args[0].request.data.get("exam", "")
        fscore = args[0].request.data.get("fscore", "")
        sscore = args[0].request.data.get("sscore", "")
        cscore = args[0].request.data.get("cscore", "")
        escore = args[0].request.data.get("escore", "")
        if not qid and not question:
            return Response(
                data={
                    "message": "Both qid and question are required to add a questions"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        staticid = args[0].request.data.get("staticid", "")
        sub_topic = args[0].request.data.get("sub_topic", "")
        if not staticid and not artist:
            return Response(
                data={
                    "message": "Both staticid and sub_topic are required to add a sub_topics"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated
