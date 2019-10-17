from googleapiclient import discovery
import os
import yaml

client = discovery.build('cloudbuild', 'v1', cache_discovery=False)


def do_build():
    params = {
            'source': {
                'storageSource': {
                    'bucket': 'louis-garman-ci-cloud-build-webhook',
                    'object': '.'
                    }
                }
            }

    params.update(yaml.load(open('cloudbuild.yaml')))

    resp = client.projects() \
            .builds() \
            .create(projectId="louis-garman-ci", body=params) \
            .execute()


def webhook(req):
    do_build()

    return 'OK'
