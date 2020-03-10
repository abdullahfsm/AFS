import pickle
import io
import time
import matplotlib.pyplot as plt
from plot import plot_show

traces = [{
    "TotalUserinfo": {
        "numOfClients": 525,
        "numOfRunningClients": 0,
        "ClientInfo": [
            {
                "stopTime": "2020-02-10 01:02:39.208+09:00",
                "clientID": "googlenet_ehSBMbk4Xo7plIH9",
                "progress": 93.68,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:34.824+09:00"
            },
            {
                "stopTime": "2020-02-10 01:38:15.753+09:00",
                "clientID": "resnet50_SyKMmnpTUIwbnb8f",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:33.087+09:00"
            },
            {
                "stopTime": "2020-02-10 02:23:43.190+09:00",
                "clientID": "inception4_YXpQJf7U4QY6tuCi",
                "progress": 99.05,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:28.429+09:00"
            },
            {
                "stopTime": "2020-02-10 02:59:49.754+09:00",
                "clientID": "inception4_r1o4YoNtggi0WCEe",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:55.941+09:00"
            },
            {
                "stopTime": "2020-02-10 01:11:04.158+09:00",
                "clientID": "vgg16_Z89UlMt6u92xQLyk",
                "progress": 97.15,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:13.517+09:00"
            },
            {
                "stopTime": "2020-02-10 02:56:45.518+09:00",
                "clientID": "inception4_cLpynJ29qz8vJmz1",
                "progress": 98.64,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:51.350+09:00"
            },
            {
                "stopTime": "2020-02-09 23:06:28.841+09:00",
                "clientID": "chatbot_n18j4nwSBj8wxq53",
                "progress": 99.5,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.270+09:00"
            },
            {
                "stopTime": "2020-02-09 23:01:54.856+09:00",
                "clientID": "chatbot_S0aHX6ZEe7VRRY7L",
                "progress": 99.56,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:06.200+09:00"
            },
            {
                "stopTime": "2020-02-10 01:57:55.782+09:00",
                "clientID": "inception4_9LtYdE9Im6aQwICa",
                "progress": 96.53,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:58.766+09:00"
            },
            {
                "stopTime": "2020-02-10 00:36:02.483+09:00",
                "clientID": "dcgan_MKP8lQTD2NxUXYDr",
                "progress": 97.94,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:00.007+09:00"
            },
            {
                "stopTime": "2020-02-10 01:27:46.717+09:00",
                "clientID": "vgg16_kyRIhjVxwuLG4jLc",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:08.150+09:00"
            },
            {
                "stopTime": "2020-02-09 23:30:36.809+09:00",
                "clientID": "video_skjbzJhFJFANWv7p",
                "progress": 99.78,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:41.437+09:00"
            },
            {
                "stopTime": "2020-02-10 01:04:44.954+09:00",
                "clientID": "googlenet_lYEKql5QoNYIvS0X",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:52.845+09:00"
            },
            {
                "stopTime": "2020-02-10 02:15:09.849+09:00",
                "clientID": "inception4_3TPvXKfnjFGLrd2K",
                "progress": 99.05,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:20.646+09:00"
            },
            {
                "stopTime": "2020-02-09 23:01:18.049+09:00",
                "clientID": "chatbot_rVaCCh4W4yWtjdDm",
                "progress": 99.62,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:24.937+09:00"
            },
            {
                "stopTime": "2020-02-10 01:42:19.153+09:00",
                "clientID": "resnet50_z2UJMGPYZA6XEBvX",
                "progress": 98.27,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:52.317+09:00"
            },
            {
                "stopTime": "2020-02-10 01:27:21.186+09:00",
                "clientID": "vgg16_vxbQI96O1on99mfW",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:06.820+09:00"
            },
            {
                "stopTime": "2020-02-10 00:02:45.206+09:00",
                "clientID": "video_OQj1AvknzkrF29tQ",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:27.192+09:00"
            },
            {
                "stopTime": "2020-02-10 03:04:22.171+09:00",
                "clientID": "inception4_9AwfwKLddnXh2EWk",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:10.536+09:00"
            },
            {
                "stopTime": "2020-02-10 00:04:34.435+09:00",
                "clientID": "video_OsLjEFPqRDC7CXCU",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:29.179+09:00"
            },
            {
                "stopTime": "2020-02-10 00:55:50.820+09:00",
                "clientID": "googlenet_oJ4ZM8kAzgcvb09K",
                "progress": 99.51,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:56.959+09:00"
            },
            {
                "stopTime": "2020-02-10 00:42:32.021+09:00",
                "clientID": "googlenet_m9W7DXy5CsSt8cE0",
                "progress": 99.17,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:47.026+09:00"
            },
            {
                "stopTime": "2020-02-10 02:18:28.826+09:00",
                "clientID": "inception4_prv4QkERvAeAjeEV",
                "progress": 98.81,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:27.913+09:00"
            },
            {
                "stopTime": "2020-02-09 23:02:30.268+09:00",
                "clientID": "chatbot_Jr2QtGJEyB3GPBgz",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:00.567+09:00"
            },
            {
                "stopTime": "2020-02-10 01:27:05.639+09:00",
                "clientID": "vgg16_PFv8mlAZd6Tsa5Kf",
                "progress": 95.45,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.171+09:00"
            },
            {
                "stopTime": "2020-02-10 01:12:55.422+09:00",
                "clientID": "vgg16_tjgZG4SjGtHDHm8Z",
                "progress": 98.27,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:16.250+09:00"
            },
            {
                "stopTime": "2020-02-10 00:53:18.140+09:00",
                "clientID": "googlenet_yOyfREy829hhImGg",
                "progress": 97.92,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:38.677+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:20.004+09:00",
                "clientID": "vgg16_L5nYfB7qSoMCnGQc",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:10.506+09:00"
            },
            {
                "stopTime": "2020-02-10 00:28:59.734+09:00",
                "clientID": "dcgan_qY0XLI3bvAWqh6iC",
                "progress": 99.49,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:18.090+09:00"
            },
            {
                "stopTime": "2020-02-10 00:15:24.950+09:00",
                "clientID": "video_eJVemiCZ7hdmyOmk",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:34.599+09:00"
            },
            {
                "stopTime": "2020-02-10 01:01:30.284+09:00",
                "clientID": "googlenet_tm1VVj72ErqGfb6s",
                "progress": 99.07,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:32.563+09:00"
            },
            {
                "stopTime": "2020-02-10 01:02:56.259+09:00",
                "clientID": "googlenet_hNTXN7Wq8eY7O45X",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:06.454+09:00"
            },
            {
                "stopTime": "2020-02-09 23:02:42.927+09:00",
                "clientID": "chatbot_iR6pFCs2sLVxGUF4",
                "progress": 97.26,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:54.529+09:00"
            },
            {
                "stopTime": "2020-02-10 02:44:47.699+09:00",
                "clientID": "inception4_Seks7seTfEfiNGf1",
                "progress": 99.51,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:06.114+09:00"
            },
            {
                "stopTime": "2020-02-10 01:33:57.299+09:00",
                "clientID": "resnet50_EXq3pLTaWgBbDsf1",
                "progress": 97.15,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:05.156+09:00"
            },
            {
                "stopTime": "2020-02-10 00:31:04.951+09:00",
                "clientID": "dcgan_AGGgislT3yA7yu50",
                "progress": 98.92,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:30.943+09:00"
            },
            {
                "stopTime": "2020-02-10 00:39:30.595+09:00",
                "clientID": "dcgan_pVxRdMUOBOmZBsKi",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:18.303+09:00"
            },
            {
                "stopTime": "2020-02-10 02:34:02.260+09:00",
                "clientID": "inception4_adVdasEhfm4iovzm",
                "progress": 98.58,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:50.276+09:00"
            },
            {
                "stopTime": "2020-02-10 00:05:58.984+09:00",
                "clientID": "video_SzNZkqLnNssbQPdt",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:32.110+09:00"
            },
            {
                "stopTime": "2020-02-10 01:30:59.314+09:00",
                "clientID": "resnet50_Hbuy8juqp0lCZVKc",
                "progress": 99.69,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:57.765+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:55.318+09:00",
                "clientID": "vgg16_Dx7oZDUIZ9ehq9sj",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.545+09:00"
            },
            {
                "stopTime": "2020-02-10 00:51:22.558+09:00",
                "clientID": "googlenet_Eb2DvkHYzQx61LWM",
                "progress": 99.2,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:36.663+09:00"
            },
            {
                "stopTime": "2020-02-10 01:06:44.008+09:00",
                "clientID": "vgg16_LzkmMaeYQ6CvI6K0",
                "progress": 99.37,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:49.346+09:00"
            },
            {
                "stopTime": "2020-02-10 02:05:41.990+09:00",
                "clientID": "inception4_3Ey15Blj8I1eaFRt",
                "progress": 97.48,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:05.819+09:00"
            },
            {
                "stopTime": "2020-02-10 00:54:35.640+09:00",
                "clientID": "googlenet_7xqhkgoVzooIrqeF",
                "progress": 97.3,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:50.190+09:00"
            },
            {
                "stopTime": "2020-02-10 01:17:23.787+09:00",
                "clientID": "vgg16_IWsTsp4YSBtBeTZg",
                "progress": 98.44,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:28.879+09:00"
            },
            {
                "stopTime": "2020-02-09 23:31:57.352+09:00",
                "clientID": "video_SnXm3oUx60CxhWWv",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:43.655+09:00"
            },
            {
                "stopTime": "2020-02-10 02:49:59.065+09:00",
                "clientID": "inception4_NDxJDynFmJE1j8Jl",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:20.685+09:00"
            },
            {
                "stopTime": "2020-02-10 00:37:50.737+09:00",
                "clientID": "dcgan_etDthJntUPFSbySG",
                "progress": 96.78,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:29.935+09:00"
            },
            {
                "stopTime": "2020-02-10 01:07:39.321+09:00",
                "clientID": "vgg16_sljET9nW17duJ2q0",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:46.118+09:00"
            },
            {
                "stopTime": "2020-02-09 23:08:53.518+09:00",
                "clientID": "chatbot_dEj46Z0LjOnkzj75",
                "progress": 98.12,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:49.836+09:00"
            },
            {
                "stopTime": "2020-02-10 03:06:38.718+09:00",
                "clientID": "inception4_FSPDVxzr4p4jtRWW",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:19.059+09:00"
            },
            {
                "stopTime": "2020-02-10 02:17:28.638+09:00",
                "clientID": "inception4_WfcnQm0wf39IAeO9",
                "progress": 99.29,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:25.501+09:00"
            },
            {
                "stopTime": "2020-02-09 23:07:52.473+09:00",
                "clientID": "chatbot_I5qZZpM1dcNnc9bQ",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.414+09:00"
            },
            {
                "stopTime": "2020-02-09 23:00:20.683+09:00",
                "clientID": "chatbot_A7bAeMLMnnI7pBGF",
                "progress": 98.99,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:18.533+09:00"
            },
            {
                "stopTime": "2020-02-10 01:02:04.991+09:00",
                "clientID": "googlenet_2HyLe6koRDYpGqG2",
                "progress": 51.89,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:34.782+09:00"
            },
            {
                "stopTime": "2020-02-10 00:23:17.564+09:00",
                "clientID": "dcgan_EOCVMKrYjNYBfXXb",
                "progress": 97.88,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:56.974+09:00"
            },
            {
                "stopTime": "2020-02-10 00:42:43.357+09:00",
                "clientID": "googlenet_LL9tLgxud2tnLdvi",
                "progress": 98.18,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:50.468+09:00"
            },
            {
                "stopTime": "2020-02-10 01:27:05.581+09:00",
                "clientID": "vgg16_43QWUNOhBXsMFEBF",
                "progress": 92.85,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.194+09:00"
            },
            {
                "stopTime": "2020-02-09 23:05:21.350+09:00",
                "clientID": "chatbot_Tc5yCvRZYWlsEueP",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.782+09:00"
            },
            {
                "stopTime": "2020-02-09 23:58:19.265+09:00",
                "clientID": "video_fezrd4HLhPdbdVou",
                "progress": 96.21,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:03.686+09:00"
            },
            {
                "stopTime": "2020-02-10 01:33:49.165+09:00",
                "clientID": "resnet50_t0NaLcx5Uh6cjrD8",
                "progress": 99.25,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:02.115+09:00"
            },
            {
                "stopTime": "2020-02-10 00:48:14.092+09:00",
                "clientID": "googlenet_4Hj7SD0Mpg9BW3cn",
                "progress": 98.49,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:06.065+09:00"
            },
            {
                "stopTime": "2020-02-10 01:26:32.555+09:00",
                "clientID": "vgg16_EkQgnkSGkCHIZTqx",
                "progress": 94.59,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.134+09:00"
            },
            {
                "stopTime": "2020-02-09 23:52:37.958+09:00",
                "clientID": "video_l62b1CRP49i7K3Q3",
                "progress": 94.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:34.994+09:00"
            },
            {
                "stopTime": "2020-02-09 23:06:53.086+09:00",
                "clientID": "chatbot_CVN7zxrTVu7sNYlI",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.632+09:00"
            },
            {
                "stopTime": "2020-02-10 01:25:13.824+09:00",
                "clientID": "vgg16_bcVwLXZgqIfLJAaU",
                "progress": 99.35,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:52.025+09:00"
            },
            {
                "stopTime": "2020-02-10 00:56:46.401+09:00",
                "clientID": "googlenet_z1WOu17AO18Vz7p0",
                "progress": 98.47,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:57.118+09:00"
            },
            {
                "stopTime": "2020-02-10 02:50:50.113+09:00",
                "clientID": "inception4_Zv4N5VospvYLgw35",
                "progress": 97.59,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:24.620+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:04.100+09:00",
                "clientID": "vgg16_TzthHaqLTFJIF5M8",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:08.193+09:00"
            },
            {
                "stopTime": "2020-02-10 00:52:26.417+09:00",
                "clientID": "googlenet_APsGoN2loFWBYUWv",
                "progress": 97.9,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:38.574+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:58.997+09:00",
                "clientID": "vgg16_FX81XHP65jhBdaj5",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:37.673+09:00"
            },
            {
                "stopTime": "2020-02-10 01:04:12.234+09:00",
                "clientID": "googlenet_MG69i37tDJ2idrYw",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.715+09:00"
            },
            {
                "stopTime": "2020-02-10 00:19:25.351+09:00",
                "clientID": "dcgan_b81d4zpRVoge3tUd",
                "progress": 98.13,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:46.366+09:00"
            },
            {
                "stopTime": "2020-02-10 02:44:20.391+09:00",
                "clientID": "inception4_VD3PYQrYoCRL5Our",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:04.080+09:00"
            },
            {
                "stopTime": "2020-02-10 00:54:06.091+09:00",
                "clientID": "googlenet_D0jVyFp5IMrymdoi",
                "progress": 99.05,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:45.412+09:00"
            },
            {
                "stopTime": "2020-02-09 23:21:50.705+09:00",
                "clientID": "video_BIBh4lXYL623IAMt",
                "progress": 98.26,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:13.356+09:00"
            },
            {
                "stopTime": "2020-02-09 23:07:26.969+09:00",
                "clientID": "chatbot_hUzuqEpud0WcfIOE",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:12.308+09:00"
            },
            {
                "stopTime": "2020-02-10 01:18:54.144+09:00",
                "clientID": "vgg16_MEEfI2oBsNrQOeuU",
                "progress": 98.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:30.859+09:00"
            },
            {
                "stopTime": "2020-02-10 01:51:53.032+09:00",
                "clientID": "resnet50_hJ5BIbkwnhEKwRZ3",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:24.290+09:00"
            },
            {
                "stopTime": "2020-02-10 01:23:15.706+09:00",
                "clientID": "vgg16_vMWe4nLCiZGhaVfo",
                "progress": 97.65,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:52.001+09:00"
            },
            {
                "stopTime": "2020-02-10 00:03:15.837+09:00",
                "clientID": "video_BkCcvupoa7ats3wo",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:29.011+09:00"
            },
            {
                "stopTime": "2020-02-10 00:39:55.933+09:00",
                "clientID": "dcgan_2UYuFFGpqbpEn6je",
                "progress": 50.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:24.596+09:00"
            },
            {
                "stopTime": "2020-02-10 02:26:57.567+09:00",
                "clientID": "inception4_nbUXRf7ZC0mrXn6m",
                "progress": 99.28,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:38.902+09:00"
            },
            {
                "stopTime": "2020-02-09 23:07:01.225+09:00",
                "clientID": "chatbot_fceVEuyF7Bkev8Wk",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.551+09:00"
            },
            {
                "stopTime": "2020-02-09 23:39:10.909+09:00",
                "clientID": "video_C7niP1VEUlRDyvMF",
                "progress": 99.57,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:52.609+09:00"
            },
            {
                "stopTime": "2020-02-10 01:47:38.168+09:00",
                "clientID": "resnet50_egzIPtUn8twSsGsI",
                "progress": 94.98,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.366+09:00"
            },
            {
                "stopTime": "2020-02-09 23:15:55.128+09:00",
                "clientID": "video_BTxRB3E3QxhRItc5",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:06.024+09:00"
            },
            {
                "stopTime": "2020-02-10 01:27:48.584+09:00",
                "clientID": "vgg16_7QAw6l2A7LIedfWy",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:08.155+09:00"
            },
            {
                "stopTime": "2020-02-10 00:08:37.158+09:00",
                "clientID": "video_JV2ZDeLBLtpSJhRV",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:18.839+09:00"
            },
            {
                "stopTime": "2020-02-10 01:22:43.118+09:00",
                "clientID": "vgg16_6aO1d4enrhMcW9VS",
                "progress": 98.7,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:51.961+09:00"
            },
            {
                "stopTime": "2020-02-10 00:41:40.920+09:00",
                "clientID": "googlenet_PITFlOOOBQo7l4Gy",
                "progress": 98.38,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:46.867+09:00"
            },
            {
                "stopTime": "2020-02-09 23:07:39.774+09:00",
                "clientID": "chatbot_oiok8ob91xJRmQdz",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.664+09:00"
            },
            {
                "stopTime": "2020-02-10 00:18:09.006+09:00",
                "clientID": "dcgan_oDEMoPHXc2cFvcDS",
                "progress": 97.82,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:46.162+09:00"
            },
            {
                "stopTime": "2020-02-10 00:39:14.247+09:00",
                "clientID": "dcgan_1sfH60HlI4taeCJX",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:10.612+09:00"
            },
            {
                "stopTime": "2020-02-10 02:35:45.174+09:00",
                "clientID": "inception4_SuXAdiO1dLcuStju",
                "progress": 92.06,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.241+09:00"
            },
            {
                "stopTime": "2020-02-10 03:01:20.906+09:00",
                "clientID": "inception4_0ensosXUkGMnQLyh",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.888+09:00"
            },
            {
                "stopTime": "2020-02-09 23:56:27.291+09:00",
                "clientID": "video_zYDA1I5cprLT4Sr6",
                "progress": 98.55,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:01.562+09:00"
            },
            {
                "stopTime": "2020-02-09 23:59:57.475+09:00",
                "clientID": "video_GMBG6VaFimna8Glu",
                "progress": 72.72,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:04.226+09:00"
            },
            {
                "stopTime": "2020-02-10 01:15:12.151+09:00",
                "clientID": "vgg16_Vs3L0wyCMoMivV6g",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:18.421+09:00"
            },
            {
                "stopTime": "2020-02-09 23:48:13.551+09:00",
                "clientID": "video_ys8YbPjhnuOP9NuY",
                "progress": 95.83,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:15.778+09:00"
            },
            {
                "stopTime": "2020-02-10 01:04:55.846+09:00",
                "clientID": "googlenet_ZSOqtSw4srneyowN",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.286+09:00"
            },
            {
                "stopTime": "2020-02-10 00:36:47.227+09:00",
                "clientID": "dcgan_Gcb3ViHHkYKZMssr",
                "progress": 96.85,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:10.629+09:00"
            },
            {
                "stopTime": "2020-02-09 23:56:33.001+09:00",
                "clientID": "video_f8R36T0hyBZptn2s",
                "progress": 94.77,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:03.349+09:00"
            },
            {
                "stopTime": "2020-02-10 01:21:29.713+09:00",
                "clientID": "vgg16_MhwvfWOPH6nQnWAY",
                "progress": 97.87,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:50.403+09:00"
            },
            {
                "stopTime": "2020-02-10 03:02:51.554+09:00",
                "clientID": "inception4_e96smJYaNa68YfOl",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.470+09:00"
            },
            {
                "stopTime": "2020-02-10 01:48:42.511+09:00",
                "clientID": "resnet50_ODd3FvPaK1QSP40c",
                "progress": 87.8,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.406+09:00"
            },
            {
                "stopTime": "2020-02-09 23:01:05.664+09:00",
                "clientID": "chatbot_WzWV5aLjnYNFUmX4",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:20.285+09:00"
            },
            {
                "stopTime": "2020-02-09 23:04:55.677+09:00",
                "clientID": "chatbot_d3WOG3VrtNSA83hV",
                "progress": 94.87,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:58.357+09:00"
            },
            {
                "stopTime": "2020-02-10 00:33:39.573+09:00",
                "clientID": "dcgan_37NgKNs81eHNHg3S",
                "progress": 97.31,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:52.414+09:00"
            },
            {
                "stopTime": "2020-02-10 00:38:24.778+09:00",
                "clientID": "dcgan_K5WL4NRe0LYoKdJa",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.219+09:00"
            },
            {
                "stopTime": "2020-02-10 01:44:36.611+09:00",
                "clientID": "resnet50_wMyySd7SxhMf1eHw",
                "progress": 97.76,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:59.720+09:00"
            },
            {
                "stopTime": "2020-02-10 01:49:36.396+09:00",
                "clientID": "resnet50_BwailsOuLrHj9SWy",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:06.671+09:00"
            },
            {
                "stopTime": "2020-02-10 01:35:44.771+09:00",
                "clientID": "resnet50_mKKDsJXqZ46xAKo1",
                "progress": 99.67,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:11.677+09:00"
            },
            {
                "stopTime": "2020-02-10 00:35:44.607+09:00",
                "clientID": "dcgan_mJwCrCbHrmr5dc2u",
                "progress": 98.48,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:57.043+09:00"
            },
            {
                "stopTime": "2020-02-10 01:09:00.770+09:00",
                "clientID": "vgg16_TZ7IyRzaDggn9yJ2",
                "progress": 97.72,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:52.464+09:00"
            },
            {
                "stopTime": "2020-02-10 01:36:47.492+09:00",
                "clientID": "resnet50_XiEnBBSVyXtVDKSW",
                "progress": 97.16,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:20.383+09:00"
            },
            {
                "stopTime": "2020-02-10 01:47:49.278+09:00",
                "clientID": "resnet50_ekN6azPtiCOCF27i",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.630+09:00"
            },
            {
                "stopTime": "2020-02-10 00:43:57.137+09:00",
                "clientID": "googlenet_ZFxJqSS6YfXa8Era",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:57.093+09:00"
            },
            {
                "stopTime": "2020-02-09 23:14:39.005+09:00",
                "clientID": "video_nWtGkBwNLmg0yMxn",
                "progress": 98.18,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:02.568+09:00"
            },
            {
                "stopTime": "2020-02-10 01:03:48.098+09:00",
                "clientID": "googlenet_gAHAUSZrZjcjGJXw",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:38.126+09:00"
            },
            {
                "stopTime": "2020-02-10 01:04:26.258+09:00",
                "clientID": "googlenet_u318sTPOXvJaEbIq",
                "progress": 50.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.863+09:00"
            },
            {
                "stopTime": "2020-02-10 00:56:44.663+09:00",
                "clientID": "googlenet_VTVie5Ca4kbx1DPq",
                "progress": 97.96,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:57.082+09:00"
            },
            {
                "stopTime": "2020-02-09 23:07:54.372+09:00",
                "clientID": "chatbot_FIuyJ5PNcFQJ1LGG",
                "progress": 99.73,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:41.185+09:00"
            },
            {
                "stopTime": "2020-02-10 01:15:02.446+09:00",
                "clientID": "vgg16_If6uInY0vc88XFiy",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:18.123+09:00"
            },
            {
                "stopTime": "2020-02-10 01:04:37.614+09:00",
                "clientID": "googlenet_2br8jDRbZna4ot1H",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:52.803+09:00"
            },
            {
                "stopTime": "2020-02-10 02:53:42.463+09:00",
                "clientID": "inception4_l9ie1JYiu085ST8j",
                "progress": 95.08,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:40.148+09:00"
            },
            {
                "stopTime": "2020-02-10 01:51:38.998+09:00",
                "clientID": "resnet50_5VcQaZ2v7t2iyJfS",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:59.655+09:00"
            },
            {
                "stopTime": "2020-02-10 01:47:29.698+09:00",
                "clientID": "resnet50_sIqCuL9TxJoreK3T",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.484+09:00"
            },
            {
                "stopTime": "2020-02-10 01:27:31.431+09:00",
                "clientID": "vgg16_CDEGfhSVkBNPVpc6",
                "progress": 93.25,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.162+09:00"
            },
            {
                "stopTime": "2020-02-09 23:08:23.246+09:00",
                "clientID": "chatbot_MUTl9P266BHwSKIA",
                "progress": 93.52,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:58.473+09:00"
            },
            {
                "stopTime": "2020-02-10 01:50:34.307+09:00",
                "clientID": "resnet50_vSfKHLFo4UgmcoUl",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.938+09:00"
            },
            {
                "stopTime": "2020-02-10 00:35:23.931+09:00",
                "clientID": "dcgan_f5JYvjOjxAgrvBin",
                "progress": 95.81,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:57.026+09:00"
            },
            {
                "stopTime": "2020-02-10 01:25:02.710+09:00",
                "clientID": "vgg16_De7PIBTt0aLQ6RAb",
                "progress": 97.5,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:25.421+09:00"
            },
            {
                "stopTime": "2020-02-10 01:49:55.394+09:00",
                "clientID": "resnet50_oc84WAp0wUWyIlVS",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.734+09:00"
            },
            {
                "stopTime": "2020-02-10 01:01:54.232+09:00",
                "clientID": "googlenet_dkV0QwenPZMmUlGF",
                "progress": 98.2,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:32.746+09:00"
            },
            {
                "stopTime": "2020-02-10 01:39:25.917+09:00",
                "clientID": "resnet50_ZdLI5jIO1lriFuSU",
                "progress": 98.72,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:36.559+09:00"
            },
            {
                "stopTime": "2020-02-10 01:25:18.687+09:00",
                "clientID": "vgg16_dqjs5TqqVaClaKFz",
                "progress": 97.22,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:17.841+09:00"
            },
            {
                "stopTime": "2020-02-10 00:58:33.296+09:00",
                "clientID": "googlenet_jtzaOBuVWIVcsCkY",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:18.003+09:00"
            },
            {
                "stopTime": "2020-02-10 01:50:34.142+09:00",
                "clientID": "resnet50_6oDWavxcESPTSOUl",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.909+09:00"
            },
            {
                "stopTime": "2020-02-10 02:13:57.374+09:00",
                "clientID": "inception4_QusYPNHl69mhHy1R",
                "progress": 99.29,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:17.656+09:00"
            },
            {
                "stopTime": "2020-02-10 01:03:35.044+09:00",
                "clientID": "googlenet_MCMVpSB2MdjKkqdK",
                "progress": 25.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.691+09:00"
            },
            {
                "stopTime": "2020-02-09 23:33:59.666+09:00",
                "clientID": "video_S1nCS9anPxxRVWMn",
                "progress": 98.9,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:45.671+09:00"
            },
            {
                "stopTime": "2020-02-09 23:08:30.161+09:00",
                "clientID": "chatbot_1kwDtsarXtMu4tza",
                "progress": 99.92,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:48.084+09:00"
            },
            {
                "stopTime": "2020-02-10 03:07:18.963+09:00",
                "clientID": "inception4_SHutcIX2WlWrnZNG",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:21.446+09:00"
            },
            {
                "stopTime": "2020-02-10 01:25:18.903+09:00",
                "clientID": "vgg16_D3ZAPTQXsFpcbOCs",
                "progress": 97.56,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:00.163+09:00"
            },
            {
                "stopTime": "2020-02-10 00:58:05.852+09:00",
                "clientID": "googlenet_o524kS3lttJJJ1DV",
                "progress": 96.94,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:07.948+09:00"
            },
            {
                "stopTime": "2020-02-09 23:12:45.833+09:00",
                "clientID": "video_PXaI3QdjSZMOMPYB",
                "progress": 98.75,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:00.235+09:00"
            },
            {
                "stopTime": "2020-02-10 00:59:17.054+09:00",
                "clientID": "googlenet_2NsIgSp58kwIfef1",
                "progress": 78.09,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.337+09:00"
            },
            {
                "stopTime": "2020-02-10 01:29:31.433+09:00",
                "clientID": "vgg16_U9s3jKQlzTsL9bNz",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.104+09:00"
            },
            {
                "stopTime": "2020-02-10 00:34:03.083+09:00",
                "clientID": "dcgan_70jnOANU5Gjn4eO7",
                "progress": 96.44,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:52.700+09:00"
            },
            {
                "stopTime": "2020-02-10 00:14:01.289+09:00",
                "clientID": "video_vBmkxzxZgS8smQWk",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:30.506+09:00"
            },
            {
                "stopTime": "2020-02-09 23:08:46.718+09:00",
                "clientID": "chatbot_nftkEoAfHb0YjUeH",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:04.296+09:00"
            },
            {
                "stopTime": "2020-02-10 01:35:39.005+09:00",
                "clientID": "resnet50_dERlbGOyZLJHcLoa",
                "progress": 98.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:17.780+09:00"
            },
            {
                "stopTime": "2020-02-09 23:58:36.703+09:00",
                "clientID": "video_TwiAWIstSdwKsluw",
                "progress": 96.17,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:03.828+09:00"
            },
            {
                "stopTime": "2020-02-09 23:03:14.547+09:00",
                "clientID": "chatbot_Nk4PfLawT7L2dH0o",
                "progress": 99.68,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:05.709+09:00"
            },
            {
                "stopTime": "2020-02-09 23:07:23.001+09:00",
                "clientID": "chatbot_3YZOSDyS4p94CFlG",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.502+09:00"
            },
            {
                "stopTime": "2020-02-10 00:05:55.304+09:00",
                "clientID": "video_Zux1uuyrk4GNYBka",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:34.334+09:00"
            },
            {
                "stopTime": "2020-02-10 01:44:49.137+09:00",
                "clientID": "resnet50_jEGNDZ3ShUQFr6EO",
                "progress": 98.17,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.139+09:00"
            },
            {
                "stopTime": "2020-02-09 23:23:22.515+09:00",
                "clientID": "video_XWSaaqxjDhp4jasq",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:18.067+09:00"
            },
            {
                "stopTime": "2020-02-10 00:54:43.037+09:00",
                "clientID": "googlenet_LP3epTwG85vB8rhQ",
                "progress": 98.75,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:55.131+09:00"
            },
            {
                "stopTime": "2020-02-10 02:56:29.471+09:00",
                "clientID": "inception4_ozeXFWmTFRHjFtJQ",
                "progress": 91.83,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:53.335+09:00"
            },
            {
                "stopTime": "2020-02-09 23:01:05.666+09:00",
                "clientID": "chatbot_qLTbaxzAipGqNAAv",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:20.488+09:00"
            },
            {
                "stopTime": "2020-02-10 02:41:38.638+09:00",
                "clientID": "inception4_orZ35SWt74Iv8fX2",
                "progress": 97.16,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.813+09:00"
            },
            {
                "stopTime": "2020-02-10 00:59:50.779+09:00",
                "clientID": "googlenet_0xOOEa9rzEnG7ymu",
                "progress": 89.18,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.511+09:00"
            },
            {
                "stopTime": "2020-02-10 02:48:38.060+09:00",
                "clientID": "inception4_3zG1WpMuPlfbFvmz",
                "progress": 98.03,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:13.729+09:00"
            },
            {
                "stopTime": "2020-02-09 22:59:03.683+09:00",
                "clientID": "chatbot_9gaz9mXofrq2Rk0c",
                "progress": 97.9,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:57.055+09:00"
            },
            {
                "stopTime": "2020-02-09 23:01:45.389+09:00",
                "clientID": "chatbot_gIkMPImqkyVx8uVo",
                "progress": 97.41,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:04.245+09:00"
            },
            {
                "stopTime": "2020-02-10 02:46:34.538+09:00",
                "clientID": "inception4_Bt98uMQfJL0D5KJL",
                "progress": 99.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:06.356+09:00"
            },
            {
                "stopTime": "2020-02-10 00:07:16.727+09:00",
                "clientID": "video_VhSTf4933Cn27Sey",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:37.653+09:00"
            },
            {
                "stopTime": "2020-02-10 00:32:34.532+09:00",
                "clientID": "dcgan_TvvvhtEifjjfdxJY",
                "progress": 93.57,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:52.110+09:00"
            },
            {
                "stopTime": "2020-02-10 00:37:55.921+09:00",
                "clientID": "dcgan_OgJxlOkKQtOVKxtF",
                "progress": 94.05,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.117+09:00"
            },
            {
                "stopTime": "2020-02-10 00:24:51.479+09:00",
                "clientID": "dcgan_qG8LvXRo8obM56Gv",
                "progress": 99.51,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:06.267+09:00"
            },
            {
                "stopTime": "2020-02-10 00:20:38.890+09:00",
                "clientID": "dcgan_pCbWL2HVlUAMj59r",
                "progress": 98.43,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:50.419+09:00"
            },
            {
                "stopTime": "2020-02-10 01:24:17.179+09:00",
                "clientID": "vgg16_z0gYkpRJkiDnUPSO",
                "progress": 98.44,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:52.230+09:00"
            },
            {
                "stopTime": "2020-02-09 23:08:46.648+09:00",
                "clientID": "chatbot_ZHoQkMxysxQHr7HB",
                "progress": 99.63,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:00.305+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:35.791+09:00",
                "clientID": "vgg16_NqPG0kFSp58rH3h7",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:18.634+09:00"
            },
            {
                "stopTime": "2020-02-10 01:51:14.565+09:00",
                "clientID": "resnet50_2A8BHpPU0AapC7wJ",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.234+09:00"
            },
            {
                "stopTime": "2020-02-10 00:31:18.688+09:00",
                "clientID": "dcgan_QJRaNxNFTxgPpP8V",
                "progress": 96.98,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:51.758+09:00"
            },
            {
                "stopTime": "2020-02-10 00:19:51.593+09:00",
                "clientID": "dcgan_YxZM7Jq6xP3FerXd",
                "progress": 99.59,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:49.168+09:00"
            },
            {
                "stopTime": "2020-02-10 00:34:42.649+09:00",
                "clientID": "dcgan_KoxUncx427xz5EO0",
                "progress": 98.27,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:54.373+09:00"
            },
            {
                "stopTime": "2020-02-10 00:50:13.452+09:00",
                "clientID": "googlenet_R296zzLWktppvHvx",
                "progress": 98.52,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:13.506+09:00"
            },
            {
                "stopTime": "2020-02-10 01:41:17.141+09:00",
                "clientID": "resnet50_qsI41WpCCb2l6Jby",
                "progress": 99.88,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:36.751+09:00"
            },
            {
                "stopTime": "2020-02-09 23:27:07.202+09:00",
                "clientID": "video_VwcQJTt8dFarNBYG",
                "progress": 99.37,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:33.358+09:00"
            },
            {
                "stopTime": "2020-02-09 23:28:39.370+09:00",
                "clientID": "video_EfWWXfOCkEXwHEU8",
                "progress": 98.12,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:35.646+09:00"
            },
            {
                "stopTime": "2020-02-10 02:57:32.009+09:00",
                "clientID": "inception4_Ml3uhIeTAwxPUZ6Q",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:55.304+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:41.685+09:00",
                "clientID": "vgg16_ggj89mCV7iy5nyRG",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.487+09:00"
            },
            {
                "stopTime": "2020-02-10 01:50:54.544+09:00",
                "clientID": "resnet50_gONRvgF0S2OX3v9t",
                "progress": 50.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:52.884+09:00"
            },
            {
                "stopTime": "2020-02-09 23:40:10.765+09:00",
                "clientID": "video_r05TUqZIZdL2uL6C",
                "progress": 98.35,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:08.353+09:00"
            },
            {
                "stopTime": "2020-02-09 23:02:31.040+09:00",
                "clientID": "chatbot_hrO95vNqPPeyk8K0",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:49.265+09:00"
            },
            {
                "stopTime": "2020-02-10 01:04:45.706+09:00",
                "clientID": "googlenet_QMniq3Dj5x3pMHtW",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:53.118+09:00"
            },
            {
                "stopTime": "2020-02-10 02:58:50.461+09:00",
                "clientID": "inception4_oCmWG6KDDrL7T6RI",
                "progress": 93.75,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:55.512+09:00"
            },
            {
                "stopTime": "2020-02-10 01:27:22.610+09:00",
                "clientID": "vgg16_BZSNlAcs8fEipj0C",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:07.030+09:00"
            },
            {
                "stopTime": "2020-02-10 02:54:27.520+09:00",
                "clientID": "inception4_J3CFk0TFGNqKfFYd",
                "progress": 94.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:41.893+09:00"
            },
            {
                "stopTime": "2020-02-09 23:35:36.322+09:00",
                "clientID": "video_kmIMI0T9yEyjrEbN",
                "progress": 96.92,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:47.480+09:00"
            },
            {
                "stopTime": "2020-02-10 00:39:28.803+09:00",
                "clientID": "dcgan_Zk8qgAjGo6PPXIEn",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:18.659+09:00"
            },
            {
                "stopTime": "2020-02-09 23:48:05.093+09:00",
                "clientID": "video_rXsLfoQLtcKq2Zan",
                "progress": 99.28,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:15.577+09:00"
            },
            {
                "stopTime": "2020-02-10 01:48:18.770+09:00",
                "clientID": "resnet50_TgMGZi53lR7vNozk",
                "progress": 92.7,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:40.676+09:00"
            },
            {
                "stopTime": "2020-02-10 01:45:41.577+09:00",
                "clientID": "resnet50_SR3eAnIrAl2uBsGd",
                "progress": 97.96,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.360+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:56.621+09:00",
                "clientID": "vgg16_T2s6FrShf1tsxHaX",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:37.731+09:00"
            },
            {
                "stopTime": "2020-02-10 01:46:46.272+09:00",
                "clientID": "resnet50_W0on7ofECIAUIIOz",
                "progress": 96.58,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:17.768+09:00"
            },
            {
                "stopTime": "2020-02-10 00:01:31.576+09:00",
                "clientID": "video_bOpxHXTp1ttEKvaR",
                "progress": 99.3,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:04.454+09:00"
            },
            {
                "stopTime": "2020-02-10 00:30:14.274+09:00",
                "clientID": "dcgan_u0juGXdhYH1zWMUg",
                "progress": 97.95,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:30.322+09:00"
            },
            {
                "stopTime": "2020-02-10 03:01:17.921+09:00",
                "clientID": "inception4_vk3Dko4IQAAr1HSg",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:21.211+09:00"
            },
            {
                "stopTime": "2020-02-10 01:44:00.128+09:00",
                "clientID": "resnet50_XYRAKGcjTQPqn08Z",
                "progress": 97.91,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:57.004+09:00"
            },
            {
                "stopTime": "2020-02-09 23:57:51.313+09:00",
                "clientID": "video_vBMtUmEn49qe8aEi",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:03.521+09:00"
            },
            {
                "stopTime": "2020-02-10 01:50:19.937+09:00",
                "clientID": "resnet50_ISW9mbkyG25wPgZo",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:47.453+09:00"
            },
            {
                "stopTime": "2020-02-10 00:51:09.678+09:00",
                "clientID": "googlenet_96qToduWFH5lkb2u",
                "progress": 99.6,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:16.210+09:00"
            },
            {
                "stopTime": "2020-02-10 00:32:50.705+09:00",
                "clientID": "dcgan_fpUNTXBMIUZjxzl3",
                "progress": 97.45,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:52.137+09:00"
            },
            {
                "stopTime": "2020-02-10 01:13:06.742+09:00",
                "clientID": "vgg16_VGtSYsLbf5HJoLH2",
                "progress": 98.8,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:13.619+09:00"
            },
            {
                "stopTime": "2020-02-09 23:32:46.109+09:00",
                "clientID": "video_0h7oAa4Ru3oampJ6",
                "progress": 98.54,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:45.346+09:00"
            },
            {
                "stopTime": "2020-02-10 01:41:57.682+09:00",
                "clientID": "resnet50_Px5ARDQ5oewJNNhw",
                "progress": 98.77,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:36.818+09:00"
            },
            {
                "stopTime": "2020-02-09 23:00:20.663+09:00",
                "clientID": "chatbot_H7OBAn7SF4TG8XwL",
                "progress": 97.93,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:52.391+09:00"
            },
            {
                "stopTime": "2020-02-09 23:05:22.015+09:00",
                "clientID": "chatbot_LhlG3ESvaRYfNbmD",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.660+09:00"
            },
            {
                "stopTime": "2020-02-10 01:12:35.221+09:00",
                "clientID": "vgg16_fh0j3b1Bhu14CD7M",
                "progress": 98.85,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:13.713+09:00"
            },
            {
                "stopTime": "2020-02-10 01:16:29.152+09:00",
                "clientID": "vgg16_jiE6x41H597AnkP1",
                "progress": 98.85,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:18.178+09:00"
            },
            {
                "stopTime": "2020-02-10 00:40:10.864+09:00",
                "clientID": "dcgan_mhZafdBF4qbWF2ti",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:44.806+09:00"
            },
            {
                "stopTime": "2020-02-10 00:44:46.326+09:00",
                "clientID": "googlenet_LZ8l84FCLBOeLJjd",
                "progress": 99.83,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:57.182+09:00"
            },
            {
                "stopTime": "2020-02-09 23:06:55.961+09:00",
                "clientID": "chatbot_4hdKOnl8eomkKi5w",
                "progress": 50.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:04.222+09:00"
            },
            {
                "stopTime": "2020-02-09 23:05:09.533+09:00",
                "clientID": "chatbot_8S32icYBYQ8G2Wtu",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:18.281+09:00"
            },
            {
                "stopTime": "2020-02-10 02:55:15.797+09:00",
                "clientID": "inception4_bZJVC7utSCnz4u5D",
                "progress": 94.73,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.905+09:00"
            },
            {
                "stopTime": "2020-02-10 00:31:56.625+09:00",
                "clientID": "dcgan_vQDzj9Unn3T6ae3m",
                "progress": 94.58,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:51.878+09:00"
            },
            {
                "stopTime": "2020-02-10 00:16:51.127+09:00",
                "clientID": "video_LxfiWJdhIBuodQhy",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 23:10:13.809+09:00"
            },
            {
                "stopTime": "2020-02-10 01:38:10.539+09:00",
                "clientID": "resnet50_8MGZ25liThU3vkXz",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:25.353+09:00"
            },
            {
                "stopTime": "2020-02-10 02:59:50.546+09:00",
                "clientID": "inception4_5067wOaiXp45mYxL",
                "progress": 92.98,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:58.031+09:00"
            },
            {
                "stopTime": "2020-02-09 23:03:04.400+09:00",
                "clientID": "chatbot_FHFgbPYu5OtHHdoQ",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:44.720+09:00"
            },
            {
                "stopTime": "2020-02-10 00:07:14.469+09:00",
                "clientID": "video_1wzdqwggds4BQd3n",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:59.309+09:00"
            },
            {
                "stopTime": "2020-02-10 00:45:53.341+09:00",
                "clientID": "googlenet_vzYGwHJldfPlyg05",
                "progress": 97.6,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:01.850+09:00"
            },
            {
                "stopTime": "2020-02-09 23:24:45.447+09:00",
                "clientID": "video_GgM3VQu93ccgm5Um",
                "progress": 98.06,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:28.700+09:00"
            },
            {
                "stopTime": "2020-02-10 02:57:29.180+09:00",
                "clientID": "inception4_R1ghrOvcvS5BcXuq",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:55.187+09:00"
            },
            {
                "stopTime": "2020-02-09 23:02:33.828+09:00",
                "clientID": "chatbot_ci6troNnCLYOJfID",
                "progress": 96.95,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:00.241+09:00"
            },
            {
                "stopTime": "2020-02-09 23:06:41.742+09:00",
                "clientID": "chatbot_tJW5dZHpScXXtpli",
                "progress": 95.29,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.478+09:00"
            },
            {
                "stopTime": "2020-02-10 00:08:32.597+09:00",
                "clientID": "video_Cjjb1GPWvW4dVIwQ",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:04.705+09:00"
            },
            {
                "stopTime": "2020-02-10 00:10:07.218+09:00",
                "clientID": "video_FT6fTaPJELL0EUAa",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:24.487+09:00"
            },
            {
                "stopTime": "2020-02-10 01:01:14.221+09:00",
                "clientID": "googlenet_0YQxhNGA8dBZpgtH",
                "progress": 97.47,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.689+09:00"
            },
            {
                "stopTime": "2020-02-10 00:23:37.630+09:00",
                "clientID": "dcgan_P72kKxPQ0IFc4DJl",
                "progress": 98.74,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:02.627+09:00"
            },
            {
                "stopTime": "2020-02-10 00:04:34.437+09:00",
                "clientID": "video_jLuV027wrRWKcP13",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:31.532+09:00"
            },
            {
                "stopTime": "2020-02-10 01:03:14.552+09:00",
                "clientID": "googlenet_tjGaTX3WDWkQG0mY",
                "progress": 97.77,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.307+09:00"
            },
            {
                "stopTime": "2020-02-10 00:40:23.358+09:00",
                "clientID": "dcgan_e9vNK5fgZ8rSYBtj",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:44.912+09:00"
            },
            {
                "stopTime": "2020-02-10 02:58:28.427+09:00",
                "clientID": "inception4_8Vp3bepK1LoqE7tS",
                "progress": 96.87,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:55.720+09:00"
            },
            {
                "stopTime": "2020-02-10 01:51:34.204+09:00",
                "clientID": "resnet50_SwfdwwOe9Ete9FTN",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:59.465+09:00"
            },
            {
                "stopTime": "2020-02-10 02:34:50.621+09:00",
                "clientID": "inception4_687JQMr1qlQyuGov",
                "progress": 97.37,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:00.482+09:00"
            },
            {
                "stopTime": "2020-02-10 00:14:05.268+09:00",
                "clientID": "video_9JjvFm0M28vxDDGH",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:34.275+09:00"
            },
            {
                "stopTime": "2020-02-09 23:06:48.940+09:00",
                "clientID": "chatbot_2c6eo2A8wQB0LTxz",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:59.802+09:00"
            },
            {
                "stopTime": "2020-02-10 00:53:30.238+09:00",
                "clientID": "googlenet_8yk7gnn3EGJgzdb8",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:45.086+09:00"
            },
            {
                "stopTime": "2020-02-10 00:21:35.246+09:00",
                "clientID": "dcgan_775KPeoom3WZqfK7",
                "progress": 99.74,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:50.901+09:00"
            },
            {
                "stopTime": "2020-02-10 02:38:02.184+09:00",
                "clientID": "inception4_7IrW2XZ2x0RA3vOc",
                "progress": 98.05,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.491+09:00"
            },
            {
                "stopTime": "2020-02-09 23:03:14.400+09:00",
                "clientID": "chatbot_5P71Gq63ynklXJnP",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:37.607+09:00"
            },
            {
                "stopTime": "2020-02-10 01:50:12.215+09:00",
                "clientID": "resnet50_nIEnvEzCMyyd40mF",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.935+09:00"
            },
            {
                "stopTime": "2020-02-09 23:01:57.582+09:00",
                "clientID": "chatbot_Yf3UDO7ACp9yAfU7",
                "progress": 99.62,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:57.152+09:00"
            },
            {
                "stopTime": "2020-02-10 01:51:14.508+09:00",
                "clientID": "resnet50_sYRJjja1CUAFnaVw",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.207+09:00"
            },
            {
                "stopTime": "2020-02-09 23:02:28.436+09:00",
                "clientID": "chatbot_dBHOvig2prKZJrAG",
                "progress": 99.56,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:49.453+09:00"
            },
            {
                "stopTime": "2020-02-10 01:25:56.043+09:00",
                "clientID": "vgg16_a62o7OL5MLLu2NC9",
                "progress": 96.87,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:29.838+09:00"
            },
            {
                "stopTime": "2020-02-09 23:05:47.572+09:00",
                "clientID": "chatbot_eUkhRzYP4Aomg8On",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:26.862+09:00"
            },
            {
                "stopTime": "2020-02-10 01:31:54.381+09:00",
                "clientID": "resnet50_Vas3fE20Mp968lB4",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:49.145+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:41.829+09:00",
                "clientID": "vgg16_3gPWx89xoIVtbihi",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.480+09:00"
            },
            {
                "stopTime": "2020-02-09 23:50:46.845+09:00",
                "clientID": "video_jyhpmKcFhh4MhhCJ",
                "progress": 96.55,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:22.097+09:00"
            },
            {
                "stopTime": "2020-02-09 23:40:55.418+09:00",
                "clientID": "video_5HBvHGl2RMJ0CyvN",
                "progress": 94.92,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:08.529+09:00"
            },
            {
                "stopTime": "2020-02-10 00:40:22.459+09:00",
                "clientID": "dcgan_rWA6uytgXMX0gool",
                "progress": -1,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.148+09:00"
            },
            {
                "stopTime": "2020-02-09 23:08:21.159+09:00",
                "clientID": "chatbot_04Io99IsWeKcfkjf",
                "progress": 98.57,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.740+09:00"
            },
            {
                "stopTime": "2020-02-10 01:25:44.150+09:00",
                "clientID": "vgg16_LJL0OESJHxHEuj88",
                "progress": 83.78,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:27.108+09:00"
            },
            {
                "stopTime": "2020-02-10 01:50:39.575+09:00",
                "clientID": "resnet50_UYmcxvZEIGDA8RZf",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:52.625+09:00"
            },
            {
                "stopTime": "2020-02-10 00:38:48.577+09:00",
                "clientID": "dcgan_hmGpfDL5XjhucWIE",
                "progress": 87.73,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.270+09:00"
            },
            {
                "stopTime": "2020-02-10 01:23:17.624+09:00",
                "clientID": "vgg16_8R3GAbznZDQ1rs03",
                "progress": 96.29,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:52.016+09:00"
            },
            {
                "stopTime": "2020-02-10 01:24:28.655+09:00",
                "clientID": "vgg16_CTRSfzXdVLS941Rz",
                "progress": 99.19,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:00.050+09:00"
            },
            {
                "stopTime": "2020-02-09 23:50:22.810+09:00",
                "clientID": "video_Xzu3PC3hL21F0jvE",
                "progress": 99.46,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:20.300+09:00"
            },
            {
                "stopTime": "2020-02-10 01:03:12.970+09:00",
                "clientID": "googlenet_Jk1Z4VSbXjxYRFdC",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:10.495+09:00"
            },
            {
                "stopTime": "2020-02-10 03:02:01.965+09:00",
                "clientID": "inception4_PTvh2RCRu3b43mzK",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:29.643+09:00"
            },
            {
                "stopTime": "2020-02-09 22:59:50.978+09:00",
                "clientID": "chatbot_CsnM0zAE98qybTdW",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:08.287+09:00"
            },
            {
                "stopTime": "2020-02-10 00:42:41.475+09:00",
                "clientID": "googlenet_Or0T6ytvHUG51D7o",
                "progress": 99.63,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:47.849+09:00"
            },
            {
                "stopTime": "2020-02-10 01:22:57.233+09:00",
                "clientID": "vgg16_yr9xvZC0u3LRIOfR",
                "progress": 98.46,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:51.883+09:00"
            },
            {
                "stopTime": "2020-02-09 23:36:53.716+09:00",
                "clientID": "video_29DXyfYIsWji95zg",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:47.901+09:00"
            },
            {
                "stopTime": "2020-02-10 00:46:49.788+09:00",
                "clientID": "googlenet_XyJV2SPhLgLU2AcM",
                "progress": 99.54,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:05.245+09:00"
            },
            {
                "stopTime": "2020-02-10 01:29:34.446+09:00",
                "clientID": "vgg16_YzhLDznZF2zqP3l2",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.127+09:00"
            },
            {
                "stopTime": "2020-02-10 00:12:41.248+09:00",
                "clientID": "video_MIfrnNuM8CkbT8d8",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:28.086+09:00"
            },
            {
                "stopTime": "2020-02-10 01:17:59.120+09:00",
                "clientID": "vgg16_wxV06ekuozJvfbTC",
                "progress": 96.42,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:30.840+09:00"
            },
            {
                "stopTime": "2020-02-10 00:00:07.746+09:00",
                "clientID": "video_1J4B2QG5sOPocknp",
                "progress": 96.94,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:03.968+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:08.704+09:00",
                "clientID": "vgg16_Cp7lCzte3rTMc9nH",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:10.433+09:00"
            },
            {
                "stopTime": "2020-02-09 23:54:37.806+09:00",
                "clientID": "video_13fJw9ZCOVpy8UUr",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:58.661+09:00"
            },
            {
                "stopTime": "2020-02-09 23:07:20.047+09:00",
                "clientID": "chatbot_JlpzBAas2x3lSxwh",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:04.360+09:00"
            },
            {
                "stopTime": "2020-02-10 01:51:36.241+09:00",
                "clientID": "resnet50_nKaa6rgQHaJaa2Ja",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:02.075+09:00"
            },
            {
                "stopTime": "2020-02-10 00:57:04.254+09:00",
                "clientID": "googlenet_fCwvVIANt53yXeUH",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:57.276+09:00"
            },
            {
                "stopTime": "2020-02-10 01:49:06.291+09:00",
                "clientID": "resnet50_kZQzEGqrh79QG8a6",
                "progress": 48.88,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.521+09:00"
            },
            {
                "stopTime": "2020-02-09 23:48:28.719+09:00",
                "clientID": "video_NR9HaW0Z4joysOXd",
                "progress": 96.7,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:15.984+09:00"
            },
            {
                "stopTime": "2020-02-09 23:05:33.539+09:00",
                "clientID": "chatbot_WGXlu0vv3dQykkoI",
                "progress": 99.54,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:58.288+09:00"
            },
            {
                "stopTime": "2020-02-10 01:14:45.027+09:00",
                "clientID": "vgg16_odu8TAAtdLIz9OjM",
                "progress": 99.23,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:16.279+09:00"
            },
            {
                "stopTime": "2020-02-10 01:03:55.377+09:00",
                "clientID": "googlenet_1yBzfCuaYElVeKdb",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:49.965+09:00"
            },
            {
                "stopTime": "2020-02-09 23:04:28.056+09:00",
                "clientID": "chatbot_UMIcnh4Rp5153389",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:13.184+09:00"
            },
            {
                "stopTime": "2020-02-10 01:00:12.359+09:00",
                "clientID": "googlenet_zfP9tnieabSUiHqN",
                "progress": 14.7,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.591+09:00"
            },
            {
                "stopTime": "2020-02-09 23:28:59.414+09:00",
                "clientID": "video_UkrR61v6j0mlhe7a",
                "progress": 98.54,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:38.468+09:00"
            },
            {
                "stopTime": "2020-02-10 01:29:16.223+09:00",
                "clientID": "vgg16_XQXnCATfYCuuVcKF",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:44.886+09:00"
            },
            {
                "stopTime": "2020-02-10 02:02:45.172+09:00",
                "clientID": "inception4_kNSpY1OqOecZerPn",
                "progress": 99.52,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:03.045+09:00"
            },
            {
                "stopTime": "2020-02-10 00:40:10.151+09:00",
                "clientID": "dcgan_JrillZUmfR3FeBPE",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:44.839+09:00"
            },
            {
                "stopTime": "2020-02-10 03:03:38.759+09:00",
                "clientID": "inception4_u90U6uVRTP2Jfx56",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:04.471+09:00"
            },
            {
                "stopTime": "2020-02-10 00:24:23.060+09:00",
                "clientID": "dcgan_SNawGYGKBBltxCCy",
                "progress": 97.9,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:05.188+09:00"
            },
            {
                "stopTime": "2020-02-10 01:22:23.525+09:00",
                "clientID": "vgg16_TIEOPk1Abg5qNalh",
                "progress": 97.82,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:51.852+09:00"
            },
            {
                "stopTime": "2020-02-10 01:27:51.736+09:00",
                "clientID": "vgg16_B9zOCB6Gy5WNw4u1",
                "progress": 98.48,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.244+09:00"
            },
            {
                "stopTime": "2020-02-10 00:29:22.971+09:00",
                "clientID": "dcgan_UJ7Bb7lUBqhsNyxO",
                "progress": 98.98,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:22.851+09:00"
            },
            {
                "stopTime": "2020-02-09 23:52:41.185+09:00",
                "clientID": "video_AjrYuTCHYB9Q1Bva",
                "progress": 93.13,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:25.127+09:00"
            },
            {
                "stopTime": "2020-02-10 02:52:36.594+09:00",
                "clientID": "inception4_P0yePwK5f8zCFBjx",
                "progress": 91.89,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:37.792+09:00"
            },
            {
                "stopTime": "2020-02-10 01:10:53.135+09:00",
                "clientID": "vgg16_FHDnr305qTGJJwRo",
                "progress": 99.11,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:06.279+09:00"
            },
            {
                "stopTime": "2020-02-10 00:38:24.442+09:00",
                "clientID": "dcgan_4x3Cs60QGSYeDq7O",
                "progress": 91.88,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.233+09:00"
            },
            {
                "stopTime": "2020-02-10 01:54:47.517+09:00",
                "clientID": "inception4_XHwGY7tLCWeZZ4Qt",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:53.394+09:00"
            },
            {
                "stopTime": "2020-02-10 00:47:19.678+09:00",
                "clientID": "googlenet_8cZXPYF3DvGO4r25",
                "progress": 97.71,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:05.370+09:00"
            },
            {
                "stopTime": "2020-02-10 01:01:34.605+09:00",
                "clientID": "googlenet_1Xu1mNsJTBPqXUzH",
                "progress": 98.7,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:32.449+09:00"
            },
            {
                "stopTime": "2020-02-09 23:25:28.411+09:00",
                "clientID": "video_gjz3R4PoMVKgFQhf",
                "progress": 98.12,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:28.851+09:00"
            },
            {
                "stopTime": "2020-02-10 01:53:01.971+09:00",
                "clientID": "inception4_ShJ19CETLNURYBlC",
                "progress": 98.23,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:51.557+09:00"
            },
            {
                "stopTime": "2020-02-09 23:13:28.188+09:00",
                "clientID": "video_zJxluPsbfsfOm3Rm",
                "progress": 98.96,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:02.041+09:00"
            },
            {
                "stopTime": "2020-02-10 00:10:07.220+09:00",
                "clientID": "video_94cLfjGz8bba562V",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:24.646+09:00"
            },
            {
                "stopTime": "2020-02-09 22:59:51.177+09:00",
                "clientID": "chatbot_nFKgejaxwUzNsQjf",
                "progress": 98.5,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:13.176+09:00"
            },
            {
                "stopTime": "2020-02-09 23:52:46.066+09:00",
                "clientID": "video_RYDAlDJY2jMcAhEH",
                "progress": 98.27,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:32.931+09:00"
            },
            {
                "stopTime": "2020-02-10 01:26:22.187+09:00",
                "clientID": "vgg16_P3yqXv09fhCJKiQy",
                "progress": 80.95,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.058+09:00"
            },
            {
                "stopTime": "2020-02-10 01:02:54.610+09:00",
                "clientID": "googlenet_alkKmWHEbEPN1auP",
                "progress": 96.71,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:47.836+09:00"
            },
            {
                "stopTime": "2020-02-10 01:04:04.277+09:00",
                "clientID": "googlenet_VYFNmQyCPzbL1gCK",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.650+09:00"
            },
            {
                "stopTime": "2020-02-10 00:15:28.898+09:00",
                "clientID": "video_mR5r3orX783mvC4h",
                "progress": 100.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:37.014+09:00"
            },
            {
                "stopTime": "2020-02-10 01:25:36.716+09:00",
                "clientID": "vgg16_VOdxi8BczHylKWDM",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:29.852+09:00"
            },
            {
                "stopTime": "2020-02-10 01:27:47.839+09:00",
                "clientID": "vgg16_B6gYXPo0xU6PaXi9",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:08.179+09:00"
            },
            {
                "stopTime": "2020-02-10 01:50:54.780+09:00",
                "clientID": "resnet50_VZgENW6jRpVGURFa",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:52.655+09:00"
            },
            {
                "stopTime": "2020-02-10 01:47:09.894+09:00",
                "clientID": "resnet50_9dpFEvWsMnCTs9o9",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.102+09:00"
            },
            {
                "stopTime": "2020-02-10 00:39:43.662+09:00",
                "clientID": "dcgan_CEsvmL97rJbZUf4N",
                "progress": -1,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.453+09:00"
            },
            {
                "stopTime": "2020-02-10 00:57:48.552+09:00",
                "clientID": "googlenet_5jxFJxZSW7fpWPZZ",
                "progress": 99.1,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.946+09:00"
            },
            {
                "stopTime": "2020-02-09 23:17:43.355+09:00",
                "clientID": "video_Il68TKN16khn4Yce",
                "progress": 98.73,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:08.497+09:00"
            },
            {
                "stopTime": "2020-02-10 02:30:47.798+09:00",
                "clientID": "inception4_v2nXZs2yXXtAQSyX",
                "progress": 99.54,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:47.671+09:00"
            },
            {
                "stopTime": "2020-02-10 03:02:07.072+09:00",
                "clientID": "inception4_eyFRg72hSMPpan2J",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:24.334+09:00"
            },
            {
                "stopTime": "2020-02-10 01:00:23.846+09:00",
                "clientID": "googlenet_sy1wJwd7ScZ8wZ4u",
                "progress": 94.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.532+09:00"
            },
            {
                "stopTime": "2020-02-10 00:59:52.819+09:00",
                "clientID": "googlenet_cwyO4kKIAK1vU4ta",
                "progress": 91.48,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.446+09:00"
            },
            {
                "stopTime": "2020-02-09 23:21:35.345+09:00",
                "clientID": "video_EcYXVtL4G08C0x33",
                "progress": 98.33,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:12.906+09:00"
            },
            {
                "stopTime": "2020-02-10 00:44:38.513+09:00",
                "clientID": "googlenet_ZjOsW1bPb9gHiQkP",
                "progress": 98.89,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:52.740+09:00"
            },
            {
                "stopTime": "2020-02-10 01:16:55.464+09:00",
                "clientID": "vgg16_QZh1iUizXgfDFLHh",
                "progress": 99.23,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:28.723+09:00"
            },
            {
                "stopTime": "2020-02-09 23:01:02.810+09:00",
                "clientID": "chatbot_7vgfjOuHRkxdW20C",
                "progress": 98.51,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:32.975+09:00"
            },
            {
                "stopTime": "2020-02-10 02:22:27.804+09:00",
                "clientID": "inception4_BUXv9CBinGKqPoHA",
                "progress": 98.82,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:28.250+09:00"
            },
            {
                "stopTime": "2020-02-09 23:43:33.674+09:00",
                "clientID": "video_KzQODPfrkNLOcfK1",
                "progress": 98.98,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:10.537+09:00"
            },
            {
                "stopTime": "2020-02-10 01:05:12.203+09:00",
                "clientID": "googlenet_Wn8M5ngEDf9jw0zd",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.319+09:00"
            },
            {
                "stopTime": "2020-02-10 01:48:45.653+09:00",
                "clientID": "resnet50_YnPV7wsagzeBaDxI",
                "progress": 95.43,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:42.020+09:00"
            },
            {
                "stopTime": "2020-02-09 23:00:35.580+09:00",
                "clientID": "chatbot_sLTVY47L9kMAuNo2",
                "progress": 98.68,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:03.716+09:00"
            },
            {
                "stopTime": "2020-02-09 23:08:53.922+09:00",
                "clientID": "chatbot_VPUlFAXVVuBT1hjG",
                "progress": 99.74,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:28.552+09:00"
            },
            {
                "stopTime": "2020-02-10 03:05:48.690+09:00",
                "clientID": "inception4_9hSc9jiCeb7ugUSA",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:18.950+09:00"
            },
            {
                "stopTime": "2020-02-10 00:12:50.871+09:00",
                "clientID": "video_BVKJmAvOPS6MVa2a",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:27.720+09:00"
            },
            {
                "stopTime": "2020-02-09 23:05:41.671+09:00",
                "clientID": "chatbot_xb1nMTNc1CB3Iz7S",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:24.203+09:00"
            },
            {
                "stopTime": "2020-02-10 03:05:04.731+09:00",
                "clientID": "inception4_7coWPMAn2HsnWBmP",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:12.866+09:00"
            },
            {
                "stopTime": "2020-02-10 01:40:00.571+09:00",
                "clientID": "resnet50_wKzSilwTAmk5ZkeF",
                "progress": 99.09,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:36.639+09:00"
            },
            {
                "stopTime": "2020-02-10 00:36:21.300+09:00",
                "clientID": "dcgan_gNY7MtfVGS4sWTAB",
                "progress": 99.09,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:00.150+09:00"
            },
            {
                "stopTime": "2020-02-10 00:47:31.313+09:00",
                "clientID": "googlenet_Q8Lj0QI22qqQYqV5",
                "progress": 99.79,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:05.346+09:00"
            },
            {
                "stopTime": "2020-02-10 02:55:30.022+09:00",
                "clientID": "inception4_mZzVtojHg9xzJo9M",
                "progress": 92.52,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:47.621+09:00"
            },
            {
                "stopTime": "2020-02-10 02:04:09.181+09:00",
                "clientID": "inception4_1PUGhsHhnFp5whsS",
                "progress": 97.77,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:03.153+09:00"
            },
            {
                "stopTime": "2020-02-09 23:04:30.364+09:00",
                "clientID": "chatbot_EqOXr3GZAMHB0WWE",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.689+09:00"
            },
            {
                "stopTime": "2020-02-10 02:08:18.666+09:00",
                "clientID": "inception4_pXXxFESPY0oQVzYG",
                "progress": 96.49,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:13.467+09:00"
            },
            {
                "stopTime": "2020-02-10 01:42:45.287+09:00",
                "clientID": "resnet50_pWlTBUWTLecRaCub",
                "progress": 93.96,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:56.876+09:00"
            },
            {
                "stopTime": "2020-02-10 00:05:52.017+09:00",
                "clientID": "video_r4Ejxyz3EUvQJMFL",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:34.566+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:07.008+09:00",
                "clientID": "vgg16_xvurhGQol2k3ypX1",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:08.188+09:00"
            },
            {
                "stopTime": "2020-02-10 00:49:44.924+09:00",
                "clientID": "googlenet_ijsBx5kj4TAz8FxX",
                "progress": 99.38,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:11.765+09:00"
            },
            {
                "stopTime": "2020-02-10 01:33:19.104+09:00",
                "clientID": "resnet50_dp5AVb5yFbY0lhvx",
                "progress": 98.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:58.033+09:00"
            },
            {
                "stopTime": "2020-02-10 00:51:43.263+09:00",
                "clientID": "googlenet_KGwRyRZVrcdlPBHD",
                "progress": 98.85,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:16.313+09:00"
            },
            {
                "stopTime": "2020-02-10 01:00:39.364+09:00",
                "clientID": "googlenet_17UwR00HMgEYhhqc",
                "progress": 95.7,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.647+09:00"
            },
            {
                "stopTime": "2020-02-10 02:29:25.505+09:00",
                "clientID": "inception4_ovh8XQHyzZG1h75S",
                "progress": 99.13,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:43.447+09:00"
            },
            {
                "stopTime": "2020-02-10 01:21:01.657+09:00",
                "clientID": "vgg16_UipEo6S1BhvTaJUS",
                "progress": 99.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:34.699+09:00"
            },
            {
                "stopTime": "2020-02-09 23:00:26.445+09:00",
                "clientID": "chatbot_T1Ebq0401GsRmXnY",
                "progress": 98.43,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:23.105+09:00"
            },
            {
                "stopTime": "2020-02-10 01:27:05.593+09:00",
                "clientID": "vgg16_NUHtj1W9r3MgARiB",
                "progress": 93.75,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.203+09:00"
            },
            {
                "stopTime": "2020-02-10 00:14:09.316+09:00",
                "clientID": "video_IKWseO9QEBdUXqxz",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:33.450+09:00"
            },
            {
                "stopTime": "2020-02-10 01:04:21.561+09:00",
                "clientID": "googlenet_gdRtgdUygJrsKt7r",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.839+09:00"
            },
            {
                "stopTime": "2020-02-10 01:43:00.552+09:00",
                "clientID": "resnet50_MmSmWndllaN01dfA",
                "progress": 97.69,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:40.847+09:00"
            },
            {
                "stopTime": "2020-02-10 00:40:35.133+09:00",
                "clientID": "dcgan_Dg5WT8ydvXVVfHfJ",
                "progress": -1,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.336+09:00"
            },
            {
                "stopTime": "2020-02-10 02:48:09.783+09:00",
                "clientID": "inception4_PxStE3mgkG7pYeah",
                "progress": 98.43,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:20.479+09:00"
            },
            {
                "stopTime": "2020-02-10 00:45:27.970+09:00",
                "clientID": "googlenet_m3Da3COCvJbZNwKv",
                "progress": 98.98,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:59.646+09:00"
            },
            {
                "stopTime": "2020-02-10 00:39:02.353+09:00",
                "clientID": "dcgan_MJQIx2q62yVPJTpW",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:08.170+09:00"
            },
            {
                "stopTime": "2020-02-09 23:56:04.791+09:00",
                "clientID": "video_bdyOjCjMq1RqSnKr",
                "progress": 87.8,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:01.259+09:00"
            },
            {
                "stopTime": "2020-02-09 23:35:39.902+09:00",
                "clientID": "video_vfnF4I39D4e5OIQq",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:45.906+09:00"
            },
            {
                "stopTime": "2020-02-10 01:29:32.527+09:00",
                "clientID": "vgg16_1mgH3gubrosaeBf1",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:46.930+09:00"
            },
            {
                "stopTime": "2020-02-10 03:05:54.690+09:00",
                "clientID": "inception4_lPtqFXnNYRyEAuUG",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:15.484+09:00"
            },
            {
                "stopTime": "2020-02-10 00:37:13.983+09:00",
                "clientID": "dcgan_6VRXAjCgf6kPdieW",
                "progress": 86.04,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:29.884+09:00"
            },
            {
                "stopTime": "2020-02-10 03:06:38.151+09:00",
                "clientID": "inception4_1BK3hD8Rt3x7nsJe",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:19.189+09:00"
            },
            {
                "stopTime": "2020-02-09 23:03:26.759+09:00",
                "clientID": "chatbot_0BKJ9k8fgO4oqg80",
                "progress": 93.63,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:40.298+09:00"
            },
            {
                "stopTime": "2020-02-10 02:37:01.335+09:00",
                "clientID": "inception4_Kvh4JwHyRorMeexS",
                "progress": 99.18,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.335+09:00"
            },
            {
                "stopTime": "2020-02-10 01:03:17.665+09:00",
                "clientID": "googlenet_oozLIaEMiLMO77QQ",
                "progress": 25.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:06.707+09:00"
            },
            {
                "stopTime": "2020-02-10 00:32:11.281+09:00",
                "clientID": "dcgan_R6XiEjMC6ZNbZaSb",
                "progress": 97.55,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:51.864+09:00"
            },
            {
                "stopTime": "2020-02-10 01:24:24.082+09:00",
                "clientID": "vgg16_04uwIZd0BwIqrN2P",
                "progress": 98.23,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:57.016+09:00"
            },
            {
                "stopTime": "2020-02-10 00:25:52.618+09:00",
                "clientID": "dcgan_LtNaDWLyWpYnYSbj",
                "progress": 99.02,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:08.308+09:00"
            },
            {
                "stopTime": "2020-02-10 01:03:37.263+09:00",
                "clientID": "googlenet_25gBj3vkO1TiBRM2",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:13.097+09:00"
            },
            {
                "stopTime": "2020-02-10 00:59:36.648+09:00",
                "clientID": "googlenet_ppsPEMRZ4KOul5Bv",
                "progress": 98.13,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.308+09:00"
            },
            {
                "stopTime": "2020-02-10 02:01:38.756+09:00",
                "clientID": "inception4_9im25Bfr44bkx7AM",
                "progress": 99.29,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:02.324+09:00"
            },
            {
                "stopTime": "2020-02-09 23:04:00.178+09:00",
                "clientID": "chatbot_bqMUeMgyugXh8ZL7",
                "progress": 99.36,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:37.982+09:00"
            },
            {
                "stopTime": "2020-02-10 02:42:52.316+09:00",
                "clientID": "inception4_Pb7bKACtL2kDPcOv",
                "progress": 98.83,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.903+09:00"
            },
            {
                "stopTime": "2020-02-10 00:01:57.226+09:00",
                "clientID": "video_Mg600ZVeUwK2cVG1",
                "progress": 96.66,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:10.835+09:00"
            },
            {
                "stopTime": "2020-02-10 00:11:21.968+09:00",
                "clientID": "video_3AdaRX0XDkndU3np",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:25.242+09:00"
            },
            {
                "stopTime": "2020-02-10 01:47:23.519+09:00",
                "clientID": "resnet50_qbig3dG6g9h4YCwD",
                "progress": 99.46,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:17.885+09:00"
            },
            {
                "stopTime": "2020-02-09 23:05:49.804+09:00",
                "clientID": "chatbot_1bOODTzxAMmkH9GX",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:24.420+09:00"
            },
            {
                "stopTime": "2020-02-10 00:25:56.700+09:00",
                "clientID": "dcgan_AIqsvrwpfkC6KxCf",
                "progress": 97.14,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:08.336+09:00"
            },
            {
                "stopTime": "2020-02-09 22:59:03.975+09:00",
                "clientID": "chatbot_cdP9niNHCcfGqBc5",
                "progress": 99.88,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:05.438+09:00"
            },
            {
                "stopTime": "2020-02-10 00:55:19.139+09:00",
                "clientID": "googlenet_WKLc3wcE8ZwZsU5S",
                "progress": 98.07,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:56.920+09:00"
            },
            {
                "stopTime": "2020-02-10 01:20:02.820+09:00",
                "clientID": "vgg16_iTa3kXP6E0SK6oAE",
                "progress": 99.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:31.014+09:00"
            },
            {
                "stopTime": "2020-02-10 03:05:08.326+09:00",
                "clientID": "inception4_mPQve0Jah3hIoHml",
                "progress": 33.33,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:12.574+09:00"
            },
            {
                "stopTime": "2020-02-10 02:51:40.430+09:00",
                "clientID": "inception4_gqCCuU2tlCR8dYyx",
                "progress": 97.56,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:24.869+09:00"
            },
            {
                "stopTime": "2020-02-09 23:03:50.356+09:00",
                "clientID": "chatbot_9kjeSQ99Tz8waknm",
                "progress": 99.56,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:15.827+09:00"
            },
            {
                "stopTime": "2020-02-10 01:10:27.124+09:00",
                "clientID": "vgg16_mL1EaqxGlr3JRCr7",
                "progress": 99.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:02.734+09:00"
            },
            {
                "stopTime": "2020-02-10 01:37:33.807+09:00",
                "clientID": "resnet50_gj4RtdzsHGKl0CZI",
                "progress": 99.14,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:24.981+09:00"
            },
            {
                "stopTime": "2020-02-10 03:00:36.660+09:00",
                "clientID": "inception4_jjylnk9x4WC8bwHU",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:12.965+09:00"
            },
            {
                "stopTime": "2020-02-09 23:07:48.257+09:00",
                "clientID": "chatbot_AdcRr3hierWBg3Of",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.766+09:00"
            },
            {
                "stopTime": "2020-02-10 03:04:22.026+09:00",
                "clientID": "inception4_9uBhq8s1w0NtIsbk",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:12.076+09:00"
            },
            {
                "stopTime": "2020-02-10 02:32:28.905+09:00",
                "clientID": "inception4_TowBhY1nNuW2mto2",
                "progress": 99.46,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:49.967+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:59.487+09:00",
                "clientID": "vgg16_SlD5YRqgQBd5Gt0W",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:37.873+09:00"
            },
            {
                "stopTime": "2020-02-10 01:17:37.457+09:00",
                "clientID": "vgg16_3tpTstq6jC3NVvb9",
                "progress": 98.83,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:28.866+09:00"
            },
            {
                "stopTime": "2020-02-10 00:07:20.923+09:00",
                "clientID": "video_o7HJXNlUttq2ugmT",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:38.609+09:00"
            },
            {
                "stopTime": "2020-02-09 23:54:32.293+09:00",
                "clientID": "video_doMqZBDns1OKZkMG",
                "progress": 98.55,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:35.385+09:00"
            },
            {
                "stopTime": "2020-02-09 23:05:37.323+09:00",
                "clientID": "chatbot_rL2CR7vHyvwyqDqK",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:24.371+09:00"
            },
            {
                "stopTime": "2020-02-09 23:38:44.487+09:00",
                "clientID": "video_BqbxmNZmlFlL2itq",
                "progress": 98.24,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:50.157+09:00"
            },
            {
                "stopTime": "2020-02-09 23:05:05.104+09:00",
                "clientID": "chatbot_C7gkhZAK6HaSQwv2",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.007+09:00"
            },
            {
                "stopTime": "2020-02-10 01:35:44.272+09:00",
                "clientID": "resnet50_D1c4wNpXWr2f0plV",
                "progress": 98.29,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:18.232+09:00"
            },
            {
                "stopTime": "2020-02-10 01:49:14.822+09:00",
                "clientID": "resnet50_APbSxQ0hqLNi1rAt",
                "progress": 98.03,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.560+09:00"
            },
            {
                "stopTime": "2020-02-10 01:29:15.079+09:00",
                "clientID": "vgg16_vk5XHfrlFVhRulbB",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:38.035+09:00"
            },
            {
                "stopTime": "2020-02-10 00:17:33.877+09:00",
                "clientID": "dcgan_lYseWmtsCazn5YKr",
                "progress": 96.96,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:44.053+09:00"
            },
            {
                "stopTime": "2020-02-09 23:00:37.805+09:00",
                "clientID": "chatbot_W7kndN5gTODMdFXr",
                "progress": 99.06,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:22.970+09:00"
            },
            {
                "stopTime": "2020-02-10 00:58:53.146+09:00",
                "clientID": "googlenet_crJ6FTSXCIkoO1GG",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:27.453+09:00"
            },
            {
                "stopTime": "2020-02-09 23:20:09.740+09:00",
                "clientID": "video_iSDkoD6Yl49rNEJF",
                "progress": 97.19,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:13.086+09:00"
            },
            {
                "stopTime": "2020-02-10 00:39:42.366+09:00",
                "clientID": "dcgan_ma81TkJq7D541RNj",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.467+09:00"
            },
            {
                "stopTime": "2020-02-09 23:06:08.848+09:00",
                "clientID": "chatbot_JDdR2133fqtwuveS",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:42.293+09:00"
            },
            {
                "stopTime": "2020-02-10 02:39:29.354+09:00",
                "clientID": "inception4_XVBnq57eEet5RBXW",
                "progress": 99.59,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.621+09:00"
            },
            {
                "stopTime": "2020-02-10 01:20:19.018+09:00",
                "clientID": "vgg16_bmN36EDQifNNYPjs",
                "progress": 99.26,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:35.445+09:00"
            },
            {
                "stopTime": "2020-02-10 02:20:15.801+09:00",
                "clientID": "inception4_Y7JGykypgU97SNd5",
                "progress": 99.52,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:28.061+09:00"
            },
            {
                "stopTime": "2020-02-10 01:00:47.376+09:00",
                "clientID": "googlenet_SDuLXSDivwBcGrSA",
                "progress": 84.56,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.713+09:00"
            },
            {
                "stopTime": "2020-02-10 00:58:57.130+09:00",
                "clientID": "googlenet_ojzA4jsnYC2wIxPY",
                "progress": 97.09,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:21.900+09:00"
            },
            {
                "stopTime": "2020-02-09 23:18:38.358+09:00",
                "clientID": "video_zCYGqBKShLJux0x5",
                "progress": 98.18,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:11.547+09:00"
            },
            {
                "stopTime": "2020-02-10 03:03:39.216+09:00",
                "clientID": "inception4_dnT5Q9xbtKqns7bC",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:07.026+09:00"
            },
            {
                "stopTime": "2020-02-09 23:50:16.836+09:00",
                "clientID": "video_aXtkcegirOZunW5C",
                "progress": 94.03,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:18.328+09:00"
            },
            {
                "stopTime": "2020-02-10 01:46:10.827+09:00",
                "clientID": "resnet50_Qc4gN4yNW5tivuRj",
                "progress": 99.74,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:07.879+09:00"
            },
            {
                "stopTime": "2020-02-10 01:49:53.519+09:00",
                "clientID": "resnet50_JZk9VjtUuv6CgwG6",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:18.468+09:00"
            },
            {
                "stopTime": "2020-02-10 00:22:25.845+09:00",
                "clientID": "dcgan_wGGeNQt0OfVXjCk5",
                "progress": 99.69,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:51.326+09:00"
            },
            {
                "stopTime": "2020-02-10 01:02:30.846+09:00",
                "clientID": "googlenet_fB9Dfse32xlm6zR0",
                "progress": 98.96,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:32.784+09:00"
            },
            {
                "stopTime": "2020-02-10 00:11:28.419+09:00",
                "clientID": "video_1bYOLPAPfyJcHaEx",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:24.871+09:00"
            },
            {
                "stopTime": "2020-02-10 02:28:50.875+09:00",
                "clientID": "inception4_9HHDgp6XF3yYOOTU",
                "progress": 98.8,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:41.043+09:00"
            },
            {
                "stopTime": "2020-02-10 01:04:28.802+09:00",
                "clientID": "googlenet_95ZRW3iZEOsi1agM",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:52.581+09:00"
            },
            {
                "stopTime": "2020-02-10 00:39:16.212+09:00",
                "clientID": "dcgan_SacEDeg2oEUmcSql",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:08.221+09:00"
            },
            {
                "stopTime": "2020-02-09 23:17:13.521+09:00",
                "clientID": "video_1xcGKbl23TxFcO7n",
                "progress": 99.58,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:08.196+09:00"
            },
            {
                "stopTime": "2020-02-10 01:49:34.491+09:00",
                "clientID": "resnet50_kACJR4ZQy9aZdDlx",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:18.340+09:00"
            },
            {
                "stopTime": "2020-02-10 00:58:35.008+09:00",
                "clientID": "googlenet_du12agGe7lUrI0wz",
                "progress": 94.44,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:18.029+09:00"
            },
            {
                "stopTime": "2020-02-09 23:46:23.437+09:00",
                "clientID": "video_ByRFTUrxcmNGkkCC",
                "progress": 99.67,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:13.439+09:00"
            },
            {
                "stopTime": "2020-02-10 00:37:08.158+09:00",
                "clientID": "dcgan_oucUi5aQwG44kZz5",
                "progress": 96.87,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:13.528+09:00"
            },
            {
                "stopTime": "2020-02-10 00:11:24.603+09:00",
                "clientID": "video_GJP1UYKrNIOlfxm9",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:24.991+09:00"
            },
            {
                "stopTime": "2020-02-09 23:06:16.901+09:00",
                "clientID": "chatbot_Nnt8HKF8eGmP3DC5",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.603+09:00"
            },
            {
                "stopTime": "2020-02-10 01:32:36.522+09:00",
                "clientID": "resnet50_ci0U6QUgQ1a1Pzcf",
                "progress": 99.35,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:57.868+09:00"
            },
            {
                "stopTime": "2020-02-10 01:32:21.919+09:00",
                "clientID": "resnet50_mLMpJabkUEiQPYRe",
                "progress": 94.1,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:57.946+09:00"
            },
            {
                "stopTime": "2020-02-09 23:07:23.005+09:00",
                "clientID": "chatbot_XZjHDPIaI0K8mZGZ",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:02.151+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:38.216+09:00",
                "clientID": "vgg16_Ie10UY5XTnsAusUf",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:18.671+09:00"
            },
            {
                "stopTime": "2020-02-10 00:56:00.433+09:00",
                "clientID": "googlenet_JU9qoi1xxrQTNw7G",
                "progress": 99.52,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:56.940+09:00"
            },
            {
                "stopTime": "2020-02-10 01:26:07.127+09:00",
                "clientID": "vgg16_V2gjuIx87ZEpZsHW",
                "progress": 95.65,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:27.525+09:00"
            },
            {
                "stopTime": "2020-02-10 02:25:43.552+09:00",
                "clientID": "inception4_16HUoeXFb3LcDheW",
                "progress": 99.29,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:32.834+09:00"
            },
            {
                "stopTime": "2020-02-10 00:10:04.801+09:00",
                "clientID": "video_eScbDua3lNNHuQ0W",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:24.753+09:00"
            },
            {
                "stopTime": "2020-02-10 00:49:34.648+09:00",
                "clientID": "googlenet_ngttPxvdQMMUq3wt",
                "progress": 99.42,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:13.129+09:00"
            },
            {
                "stopTime": "2020-02-09 23:04:37.517+09:00",
                "clientID": "chatbot_06SWGU6BFQVlLcAv",
                "progress": 98.98,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:34.862+09:00"
            },
            {
                "stopTime": "2020-02-09 23:43:57.033+09:00",
                "clientID": "video_NMSfHmpZIuJby98E",
                "progress": 99.42,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:11.311+09:00"
            },
            {
                "stopTime": "2020-02-10 01:46:22.853+09:00",
                "clientID": "resnet50_VFdC9rF0k25iGwTo",
                "progress": 97.03,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:15.628+09:00"
            },
            {
                "stopTime": "2020-02-10 01:09:21.031+09:00",
                "clientID": "vgg16_DmNL29ioT7C050Ln",
                "progress": 99.62,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:46.264+09:00"
            },
            {
                "stopTime": "2020-02-10 01:50:14.430+09:00",
                "clientID": "resnet50_llmnbOB8vIRe1vsU",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:26.674+09:00"
            },
            {
                "stopTime": "2020-02-10 01:21:37.426+09:00",
                "clientID": "vgg16_9nQgkwOCcrxyWMB1",
                "progress": 97.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:51.831+09:00"
            },
            {
                "stopTime": "2020-02-09 23:06:46.038+09:00",
                "clientID": "chatbot_PbRjM8BodzDMKNjw",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.870+09:00"
            },
            {
                "stopTime": "2020-02-10 01:40:12.590+09:00",
                "clientID": "resnet50_Iw8JkUB71a3rSJNe",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:36.608+09:00"
            },
            {
                "stopTime": "2020-02-10 00:27:16.058+09:00",
                "clientID": "dcgan_aQwL2H4jkPWfp1CG",
                "progress": 99.57,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:16.264+09:00"
            },
            {
                "stopTime": "2020-02-10 01:26:30.554+09:00",
                "clientID": "vgg16_hmVSTwkFn2c2V85F",
                "progress": 96.96,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:29.859+09:00"
            },
            {
                "stopTime": "2020-02-09 23:05:57.781+09:00",
                "clientID": "chatbot_HxaVJz5DoYSChHQB",
                "progress": 50.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:26.908+09:00"
            },
            {
                "stopTime": "2020-02-09 23:03:01.584+09:00",
                "clientID": "chatbot_wcAvz65uhLEcwK9l",
                "progress": 96.65,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:59.976+09:00"
            },
            {
                "stopTime": "2020-02-09 23:04:43.109+09:00",
                "clientID": "chatbot_VCdcIojp8HpE0oA1",
                "progress": 98.71,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:36.716+09:00"
            },
            {
                "stopTime": "2020-02-09 23:06:18.000+09:00",
                "clientID": "chatbot_8fjqnFKd0pbyTWsU",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:46.915+09:00"
            },
            {
                "stopTime": "2020-02-09 23:09:40.765+09:00",
                "clientID": "video_9a8g0ARq66sHB935",
                "progress": 99.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:53.755+09:00"
            },
            {
                "stopTime": "2020-02-10 02:40:16.010+09:00",
                "clientID": "inception4_EeXW45VzOxkIYwzg",
                "progress": 99.16,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.714+09:00"
            },
            {
                "stopTime": "2020-02-10 01:48:14.284+09:00",
                "clientID": "resnet50_o5ntacbhKC2uC6hG",
                "progress": 95.14,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.563+09:00"
            },
            {
                "stopTime": "2020-02-09 22:58:49.499+09:00",
                "clientID": "chatbot_EbkxSiaP8EHHJ1Kz",
                "progress": 95.67,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:56.266+09:00"
            },
            {
                "stopTime": "2020-02-10 00:37:27.898+09:00",
                "clientID": "dcgan_sfaBgJZzwNDnMUSx",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:29.896+09:00"
            },
            {
                "stopTime": "2020-02-10 01:44:52.693+09:00",
                "clientID": "resnet50_u2NwLfZfpbvyl3JS",
                "progress": 98.75,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:00.042+09:00"
            },
            {
                "stopTime": "2020-02-10 00:40:34.952+09:00",
                "clientID": "dcgan_1VnH5WnU52e7hZoX",
                "progress": -1,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.179+09:00"
            },
            {
                "stopTime": "2020-02-10 00:16:44.102+09:00",
                "clientID": "video_JMKVgPQlBBFdv03A",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:37.525+09:00"
            },
            {
                "stopTime": "2020-02-10 01:09:15.640+09:00",
                "clientID": "vgg16_BWA5iyTHOO78raVY",
                "progress": 98.12,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:58.121+09:00"
            },
            {
                "stopTime": "2020-02-09 23:07:08.562+09:00",
                "clientID": "chatbot_JWEH3hitd7OJhRw3",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.720+09:00"
            },
            {
                "stopTime": "2020-02-10 01:30:48.856+09:00",
                "clientID": "resnet50_hobA097FePEvn5VC",
                "progress": 97.89,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:47.279+09:00"
            },
            {
                "stopTime": "2020-02-09 23:04:46.378+09:00",
                "clientID": "chatbot_qlmykyTOHmxJaRcM",
                "progress": 98.27,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:00.384+09:00"
            },
            {
                "stopTime": "2020-02-10 01:21:54.115+09:00",
                "clientID": "vgg16_kDjbYMXtP5zkFMrE",
                "progress": 99.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:33.152+09:00"
            },
            {
                "stopTime": "2020-02-09 23:54:32.208+09:00",
                "clientID": "video_hmntYcia0hKsXpH3",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:51.188+09:00"
            },
            {
                "stopTime": "2020-02-10 00:57:42.022+09:00",
                "clientID": "googlenet_qK6QImXqbzbAzekT",
                "progress": 98.68,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:03.525+09:00"
            },
            {
                "stopTime": "2020-02-10 00:39:58.003+09:00",
                "clientID": "dcgan_BYYkiEpH9Rb6hb5G",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.511+09:00"
            },
            {
                "stopTime": "2020-02-10 00:39:00.786+09:00",
                "clientID": "dcgan_UqVGqI7I3hgWxdii",
                "progress": -1,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:06.539+09:00"
            },
            {
                "stopTime": "2020-02-10 03:00:31.665+09:00",
                "clientID": "inception4_15FCrr7nJNfuaI0M",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.418+09:00"
            },
            {
                "stopTime": "2020-02-09 23:06:04.970+09:00",
                "clientID": "chatbot_XPNztJf0eLaDFGgE",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:16.173+09:00"
            },
            {
                "stopTime": "2020-02-09 23:45:15.179+09:00",
                "clientID": "video_hNOLjfoR1A3UoIWy",
                "progress": 98.31,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:13.189+09:00"
            },
            {
                "stopTime": "2020-02-10 01:59:22.367+09:00",
                "clientID": "inception4_WuMmS4577duEhaeO",
                "progress": 99.59,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:59.743+09:00"
            },
            {
                "stopTime": "2020-02-10 01:48:04.565+09:00",
                "clientID": "resnet50_XKYxDGeO3eRtad0w",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:32.614+09:00"
            },
            {
                "stopTime": "2020-02-10 00:38:38.357+09:00",
                "clientID": "dcgan_v4MR4BGNkWQpSazn",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.761+09:00"
            },
            {
                "stopTime": "2020-02-10 01:29:15.495+09:00",
                "clientID": "vgg16_YiXibDd06F734H9o",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:37.897+09:00"
            },
            {
                "stopTime": "2020-02-10 01:06:51.333+09:00",
                "clientID": "vgg16_VETB0FkXeJQOeVbE",
                "progress": 99.23,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:45.391+09:00"
            },
            {
                "stopTime": "2020-02-10 01:08:08.200+09:00",
                "clientID": "vgg16_Tn6z175hdN6qtXLD",
                "progress": 96.32,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:58.074+09:00"
            },
            {
                "stopTime": "2020-02-09 23:03:11.783+09:00",
                "clientID": "chatbot_K2esqpC0J1usSjQG",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:08.128+09:00"
            },
            {
                "stopTime": "2020-02-10 00:04:31.920+09:00",
                "clientID": "video_5AXX4SikOc1nQv4T",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:31.824+09:00"
            },
            {
                "stopTime": "2020-02-10 02:07:19.833+09:00",
                "clientID": "inception4_JGPQlXVFZrG2rdSj",
                "progress": 99.76,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:08.637+09:00"
            },
            {
                "stopTime": "2020-02-09 23:42:23.895+09:00",
                "clientID": "video_CusZJ7eZol7yEi3K",
                "progress": 97.58,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:08.703+09:00"
            },
            {
                "stopTime": "2020-02-10 00:12:44.100+09:00",
                "clientID": "video_QT6D3WADEYBH6X39",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:27.413+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:23.936+09:00",
                "clientID": "vgg16_FVHIyCKJoUq82pgl",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:18.512+09:00"
            },
            {
                "stopTime": "2020-02-10 00:15:21.469+09:00",
                "clientID": "video_xAPwXdfRqkRAKHR4",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:37.216+09:00"
            },
            {
                "stopTime": "2020-02-09 22:59:09.270+09:00",
                "clientID": "chatbot_yBFU2mI4FqboDWw4",
                "progress": 97.76,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:04.380+09:00"
            },
            {
                "stopTime": "2020-02-10 00:01:23.321+09:00",
                "clientID": "video_dpg8nvkIwQTX5x8l",
                "progress": 80.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:24.584+09:00"
            },
            {
                "stopTime": "2020-02-10 01:57:02.297+09:00",
                "clientID": "inception4_PdMdUg9o4tIJdwSH",
                "progress": 97.29,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:56.161+09:00"
            },
            {
                "stopTime": "2020-02-10 01:51:17.956+09:00",
                "clientID": "resnet50_DeSfTJ3xBeoJSHNW",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:55.363+09:00"
            },
            {
                "stopTime": "2020-02-10 01:50:59.203+09:00",
                "clientID": "resnet50_aQUUncXrW5aCil3y",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:53.052+09:00"
            },
            {
                "stopTime": "2020-02-10 00:27:41.404+09:00",
                "clientID": "dcgan_cT01nHxeYZEiXPtL",
                "progress": 98.28,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:13.704+09:00"
            },
            {
                "stopTime": "2020-02-10 01:18:50.814+09:00",
                "clientID": "vgg16_zrX5ke666dwQoKyU",
                "progress": 98.66,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:30.931+09:00"
            },
            {
                "stopTime": "2020-02-10 01:04:07.594+09:00",
                "clientID": "googlenet_7LGgZ4aDd64FDm2g",
                "progress": 25.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:38.259+09:00"
            },
            {
                "stopTime": "2020-02-10 00:08:50.045+09:00",
                "clientID": "video_RPYLhBu4Vc3woARO",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:57:09.684+09:00"
            },
            {
                "stopTime": "2020-02-10 01:29:14.286+09:00",
                "clientID": "vgg16_pqsWnyTNr3SJFixZ",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:37.988+09:00"
            },
            {
                "stopTime": "2020-02-10 01:29:32.323+09:00",
                "clientID": "vgg16_9l5HTMbumhRIjIsC",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:50.351+09:00"
            },
            {
                "stopTime": "2020-02-09 23:11:50.682+09:00",
                "clientID": "video_EXdMOpVVtpKfu4Fi",
                "progress": 99.17,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:59.606+09:00"
            },
            {
                "stopTime": "2020-02-10 01:55:47.899+09:00",
                "clientID": "inception4_7KD0qAlMxn8iNVno",
                "progress": 97.95,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:53:55.950+09:00"
            },
            {
                "stopTime": "2020-02-10 01:01:45.850+09:00",
                "clientID": "googlenet_j4lNsEbZRtB9X8gT",
                "progress": 96.62,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:32.639+09:00"
            },
            {
                "stopTime": "2020-02-10 01:28:25.091+09:00",
                "clientID": "vgg16_YBfVnyu2vfEQJmOI",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:18.484+09:00"
            },
            {
                "stopTime": "2020-02-10 02:11:24.466+09:00",
                "clientID": "inception4_g3Tji7aDNnWa9JOo",
                "progress": 98.82,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:16.155+09:00"
            },
            {
                "stopTime": "2020-02-10 02:52:30.819+09:00",
                "clientID": "inception4_nN7AApHVpPN274to",
                "progress": 97.45,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:30.043+09:00"
            },
            {
                "stopTime": "2020-02-10 01:50:00.728+09:00",
                "clientID": "resnet50_T6RmuvEUNbmXczUs",
                "progress": 98.67,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:58.408+09:00"
            },
            {
                "stopTime": "2020-02-10 01:49:05.492+09:00",
                "clientID": "resnet50_4IF5gdnrflPnT2rj",
                "progress": 95.83,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:44.890+09:00"
            },
            {
                "stopTime": "2020-02-10 02:46:42.807+09:00",
                "clientID": "inception4_tGb71UmWRri1hZPf",
                "progress": 95.65,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:08.062+09:00"
            },
            {
                "stopTime": "2020-02-09 23:45:48.440+09:00",
                "clientID": "video_TNsscJ6k246e7vHo",
                "progress": 98.62,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:15.404+09:00"
            },
            {
                "stopTime": "2020-02-10 03:02:55.026+09:00",
                "clientID": "inception4_FlC8KEvaYAKPIDZq",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:59.615+09:00"
            },
            {
                "stopTime": "2020-02-10 01:43:37.628+09:00",
                "clientID": "resnet50_9awGTpyd6bUT3xni",
                "progress": 94.21,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:57.147+09:00"
            },
            {
                "stopTime": "2020-02-10 01:41:23.088+09:00",
                "clientID": "resnet50_rwnTUi3kmsIbi2RQ",
                "progress": 99.49,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:39.023+09:00"
            },
            {
                "stopTime": "2020-02-10 01:13:20.474+09:00",
                "clientID": "vgg16_IpaUBh6MBdGKJCpW",
                "progress": 99.61,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:16.235+09:00"
            },
            {
                "stopTime": "2020-02-09 23:03:41.770+09:00",
                "clientID": "chatbot_VOCHMKG3w4BqrF36",
                "progress": 84.37,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:50.378+09:00"
            },
            {
                "stopTime": "2020-02-09 23:06:26.021+09:00",
                "clientID": "chatbot_GWfldr3OLEIs6oJg",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:40.494+09:00"
            },
            {
                "stopTime": "2020-02-10 01:03:32.122+09:00",
                "clientID": "googlenet_9BKHj6td2S62aAtT",
                "progress": 0.0,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:56:20.582+09:00"
            },
            {
                "stopTime": "2020-02-10 01:45:33.882+09:00",
                "clientID": "resnet50_SXDIUM9WUGcplnIT",
                "progress": 100.0,
                "status": "Completed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:08.193+09:00"
            },
            {
                "stopTime": "2020-02-10 00:59:20.290+09:00",
                "clientID": "googlenet_XAtj13kzyXSXgfea",
                "progress": 97.36,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:55:27.509+09:00"
            },
            {
                "stopTime": "2020-02-10 02:09:53.254+09:00",
                "clientID": "inception4_i0ycpq6dhCAqb7xR",
                "progress": 98.78,
                "status": "Killed",
                "clientGPUList": {},
                "startTime": "2020-02-09 22:54:16.031+09:00"
            }
        ]
    }
},
{
    "TotalUserinfo": {
        "numOfClients": 525,
        "numOfRunningClients": 0,
        "ClientInfo": [
            {
                "clientID": "vgg16_z0gYkpRJkiDnUPSO",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:59.345+09:00",
                "progress": 99.22,
                "stopTime": "2020-02-09 21:53:51.265+09:00"
            },
            {
                "clientID": "vgg16_NUHtj1W9r3MgARiB",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:31.388+09:00",
                "progress": 96.87,
                "stopTime": "2020-02-09 21:49:27.350+09:00"
            },
            {
                "clientID": "chatbot_ZHoQkMxysxQHr7HB",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:51.583+09:00",
                "progress": 99.9,
                "stopTime": "2020-02-09 21:17:39.411+09:00"
            },
            {
                "clientID": "vgg16_iTa3kXP6E0SK6oAE",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:25.074+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:59:45.314+09:00"
            },
            {
                "clientID": "googlenet_Or0T6ytvHUG51D7o",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:50.084+09:00",
                "progress": 99.91,
                "stopTime": "2020-02-09 21:32:41.323+09:00"
            },
            {
                "clientID": "googlenet_gdRtgdUygJrsKt7r",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:15.348+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:26:49.641+09:00"
            },
            {
                "clientID": "resnet50_6oDWavxcESPTSOUl",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:12.165+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:42.771+09:00"
            },
            {
                "clientID": "resnet50_gONRvgF0S2OX3v9t",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:17.608+09:00",
                "progress": 87.5,
                "stopTime": "2020-02-09 21:33:49.661+09:00"
            },
            {
                "clientID": "video_OsLjEFPqRDC7CXCU",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:56.218+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:44:06.671+09:00"
            },
            {
                "clientID": "vgg16_TIEOPk1Abg5qNalh",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:57.401+09:00",
                "progress": 99.27,
                "stopTime": "2020-02-09 21:54:31.863+09:00"
            },
            {
                "clientID": "video_r4Ejxyz3EUvQJMFL",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:47.396+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:44:25.477+09:00"
            },
            {
                "clientID": "googlenet_z1WOu17AO18Vz7p0",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:00.718+09:00",
                "progress": 99.3,
                "stopTime": "2020-02-09 21:25:35.286+09:00"
            },
            {
                "clientID": "inception4_7coWPMAn2HsnWBmP",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:21.123+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:08:20.858+09:00"
            },
            {
                "clientID": "inception4_SuXAdiO1dLcuStju",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:16.063+09:00",
                "progress": 99.2,
                "stopTime": "2020-02-09 22:12:21.688+09:00"
            },
            {
                "clientID": "inception4_PxStE3mgkG7pYeah",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:16.493+09:00",
                "progress": 99.21,
                "stopTime": "2020-02-09 22:12:03.753+09:00"
            },
            {
                "clientID": "vgg16_FX81XHP65jhBdaj5",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:48.721+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:49:50.903+09:00"
            },
            {
                "clientID": "inception4_BUXv9CBinGKqPoHA",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:39.356+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 22:35:34.760+09:00"
            },
            {
                "clientID": "dcgan_sfaBgJZzwNDnMUSx",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:38.394+09:00",
                "progress": 86.66,
                "stopTime": "2020-02-09 21:17:34.502+09:00"
            },
            {
                "clientID": "dcgan_mhZafdBF4qbWF2ti",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:12.370+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:17:51.849+09:00"
            },
            {
                "clientID": "video_rXsLfoQLtcKq2Zan",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:02.947+09:00",
                "progress": 99.64,
                "stopTime": "2020-02-09 21:44:04.124+09:00"
            },
            {
                "clientID": "dcgan_cT01nHxeYZEiXPtL",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:28.224+09:00",
                "progress": 99.84,
                "stopTime": "2020-02-09 21:25:09.371+09:00"
            },
            {
                "clientID": "googlenet_PITFlOOOBQo7l4Gy",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:49.186+09:00",
                "progress": 99.57,
                "stopTime": "2020-02-09 21:25:36.952+09:00"
            },
            {
                "clientID": "resnet50_SXDIUM9WUGcplnIT",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:05.771+09:00",
                "progress": 99.14,
                "stopTime": "2020-02-09 21:32:38.108+09:00"
            },
            {
                "clientID": "googlenet_sy1wJwd7ScZ8wZ4u",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:16.793+09:00",
                "progress": 99.69,
                "stopTime": "2020-02-09 21:26:56.728+09:00"
            },
            {
                "clientID": "resnet50_z2UJMGPYZA6XEBvX",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:44.925+09:00",
                "progress": 99.42,
                "stopTime": "2020-02-09 21:34:09.094+09:00"
            },
            {
                "clientID": "resnet50_EXq3pLTaWgBbDsf1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:20.251+09:00",
                "progress": 99.82,
                "stopTime": "2020-02-09 21:36:23.819+09:00"
            },
            {
                "clientID": "chatbot_1kwDtsarXtMu4tza",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:46.765+09:00",
                "progress": 99.92,
                "stopTime": "2020-02-09 21:17:23.630+09:00"
            },
            {
                "clientID": "googlenet_tjGaTX3WDWkQG0mY",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:32.877+09:00",
                "progress": 99.65,
                "stopTime": "2020-02-09 21:29:09.946+09:00"
            },
            {
                "clientID": "video_9a8g0ARq66sHB935",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:00.951+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:41:28.842+09:00"
            },
            {
                "clientID": "googlenet_fB9Dfse32xlm6zR0",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:12.844+09:00",
                "progress": 99.53,
                "stopTime": "2020-02-09 21:28:09.056+09:00"
            },
            {
                "clientID": "chatbot_cdP9niNHCcfGqBc5",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:04.716+09:00",
                "progress": 98.56,
                "stopTime": "2020-02-09 21:16:47.261+09:00"
            },
            {
                "clientID": "vgg16_tjgZG4SjGtHDHm8Z",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:25.095+09:00",
                "progress": 99.42,
                "stopTime": "2020-02-09 21:54:32.613+09:00"
            },
            {
                "clientID": "chatbot_rVaCCh4W4yWtjdDm",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:35.255+09:00",
                "progress": 99.43,
                "stopTime": "2020-02-09 21:17:50.075+09:00"
            },
            {
                "clientID": "video_TNsscJ6k246e7vHo",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:06.487+09:00",
                "progress": 98.62,
                "stopTime": "2020-02-09 21:40:35.130+09:00"
            },
            {
                "clientID": "video_Zux1uuyrk4GNYBka",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:04.559+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:44:07.017+09:00"
            },
            {
                "clientID": "chatbot_0BKJ9k8fgO4oqg80",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:29.401+09:00",
                "progress": 98.63,
                "stopTime": "2020-02-09 21:15:53.695+09:00"
            },
            {
                "clientID": "resnet50_XiEnBBSVyXtVDKSW",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:32.071+09:00",
                "progress": 99.78,
                "stopTime": "2020-02-09 21:35:04.782+09:00"
            },
            {
                "clientID": "dcgan_MKP8lQTD2NxUXYDr",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:07.371+09:00",
                "progress": 99.31,
                "stopTime": "2020-02-09 21:19:56.316+09:00"
            },
            {
                "clientID": "chatbot_4hdKOnl8eomkKi5w",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:13.783+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:16:13.013+09:00"
            },
            {
                "clientID": "resnet50_wMyySd7SxhMf1eHw",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:46.528+09:00",
                "progress": 99.86,
                "stopTime": "2020-02-09 21:40:58.486+09:00"
            },
            {
                "clientID": "video_SnXm3oUx60CxhWWv",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:42.452+09:00",
                "progress": 99.78,
                "stopTime": "2020-02-09 21:45:51.807+09:00"
            },
            {
                "clientID": "video_VhSTf4933Cn27Sey",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:12.620+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:45:01.950+09:00"
            },
            {
                "clientID": "inception4_Ml3uhIeTAwxPUZ6Q",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:41.981+09:00",
                "progress": 75.0,
                "stopTime": "2020-02-09 22:00:57.233+09:00"
            },
            {
                "clientID": "dcgan_AIqsvrwpfkC6KxCf",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:30.908+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:22:07.324+09:00"
            },
            {
                "clientID": "dcgan_SacEDeg2oEUmcSql",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:44.744+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:17:29.482+09:00"
            },
            {
                "clientID": "chatbot_XZjHDPIaI0K8mZGZ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:26.843+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:38.646+09:00"
            },
            {
                "clientID": "inception4_9uBhq8s1w0NtIsbk",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:13.992+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:07:10.704+09:00"
            },
            {
                "clientID": "video_Cjjb1GPWvW4dVIwQ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:09.122+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:44:41.182+09:00"
            },
            {
                "clientID": "dcgan_SNawGYGKBBltxCCy",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:16.644+09:00",
                "progress": 99.58,
                "stopTime": "2020-02-09 21:21:54.844+09:00"
            },
            {
                "clientID": "video_vBMtUmEn49qe8aEi",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:47.756+09:00",
                "progress": 97.36,
                "stopTime": "2020-02-09 21:44:45.085+09:00"
            },
            {
                "clientID": "inception4_mPQve0Jah3hIoHml",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:22.501+09:00",
                "progress": 66.66,
                "stopTime": "2020-02-09 22:08:34.381+09:00"
            },
            {
                "clientID": "chatbot_H7OBAn7SF4TG8XwL",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:57.199+09:00",
                "progress": 99.27,
                "stopTime": "2020-02-09 21:15:26.764+09:00"
            },
            {
                "clientID": "resnet50_Qc4gN4yNW5tivuRj",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:10.481+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:35:49.799+09:00"
            },
            {
                "clientID": "vgg16_9nQgkwOCcrxyWMB1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:58.122+09:00",
                "progress": 99.2,
                "stopTime": "2020-02-09 21:53:34.626+09:00"
            },
            {
                "clientID": "dcgan_EOCVMKrYjNYBfXXb",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:01.816+09:00",
                "progress": 99.89,
                "stopTime": "2020-02-09 21:25:35.574+09:00"
            },
            {
                "clientID": "video_OQj1AvknzkrF29tQ",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:03.212+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:44:12.211+09:00"
            },
            {
                "clientID": "chatbot_UMIcnh4Rp5153389",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:52.924+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:15:31.320+09:00"
            },
            {
                "clientID": "inception4_u90U6uVRTP2Jfx56",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:14.102+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:08:26.062+09:00"
            },
            {
                "clientID": "resnet50_Vas3fE20Mp968lB4",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:50.480+09:00",
                "progress": 99.89,
                "stopTime": "2020-02-09 21:41:57.079+09:00"
            },
            {
                "clientID": "video_NMSfHmpZIuJby98E",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:54.479+09:00",
                "progress": 99.71,
                "stopTime": "2020-02-09 21:48:21.454+09:00"
            },
            {
                "clientID": "chatbot_hrO95vNqPPeyk8K0",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:54.348+09:00",
                "progress": 99.12,
                "stopTime": "2020-02-09 21:18:02.300+09:00"
            },
            {
                "clientID": "resnet50_2A8BHpPU0AapC7wJ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:15.398+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:39.956+09:00"
            },
            {
                "clientID": "vgg16_QZh1iUizXgfDFLHh",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:29.998+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:59:32.991+09:00"
            },
            {
                "clientID": "dcgan_fpUNTXBMIUZjxzl3",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:01.561+09:00",
                "progress": 99.63,
                "stopTime": "2020-02-09 21:19:53.279+09:00"
            },
            {
                "clientID": "chatbot_04Io99IsWeKcfkjf",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:40.370+09:00",
                "progress": 95.37,
                "stopTime": "2020-02-09 21:16:42.895+09:00"
            },
            {
                "clientID": "inception4_9im25Bfr44bkx7AM",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:19.450+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:33:49.180+09:00"
            },
            {
                "clientID": "vgg16_a62o7OL5MLLu2NC9",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:31.393+09:00",
                "progress": 96.87,
                "stopTime": "2020-02-09 21:49:32.629+09:00"
            },
            {
                "clientID": "vgg16_xvurhGQol2k3ypX1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:45.047+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:07.640+09:00"
            },
            {
                "clientID": "video_GJP1UYKrNIOlfxm9",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:25.392+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:46:13.100+09:00"
            },
            {
                "clientID": "inception4_kNSpY1OqOecZerPn",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:09.925+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:32:32.979+09:00"
            },
            {
                "clientID": "vgg16_7QAw6l2A7LIedfWy",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:36.429+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:48:48.654+09:00"
            },
            {
                "clientID": "inception4_prv4QkERvAeAjeEV",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:37.708+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:32:23.332+09:00"
            },
            {
                "clientID": "vgg16_bmN36EDQifNNYPjs",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:31.210+09:00",
                "progress": 99.26,
                "stopTime": "2020-02-09 21:53:29.353+09:00"
            },
            {
                "clientID": "resnet50_hJ5BIbkwnhEKwRZ3",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:14.901+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:31.355+09:00"
            },
            {
                "clientID": "video_MIfrnNuM8CkbT8d8",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:22.862+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:46:54.097+09:00"
            },
            {
                "clientID": "googlenet_96qToduWFH5lkb2u",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:27.055+09:00",
                "progress": 99.77,
                "stopTime": "2020-02-09 21:29:52.350+09:00"
            },
            {
                "clientID": "googlenet_2HyLe6koRDYpGqG2",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:40.410+09:00",
                "progress": 94.93,
                "stopTime": "2020-02-09 21:26:20.796+09:00"
            },
            {
                "clientID": "googlenet_4Hj7SD0Mpg9BW3cn",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:20.349+09:00",
                "progress": 99.93,
                "stopTime": "2020-02-09 21:28:01.441+09:00"
            },
            {
                "clientID": "resnet50_W0on7ofECIAUIIOz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:13.071+09:00",
                "progress": 99.51,
                "stopTime": "2020-02-09 21:36:23.840+09:00"
            },
            {
                "clientID": "dcgan_mJwCrCbHrmr5dc2u",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:47.174+09:00",
                "progress": 99.52,
                "stopTime": "2020-02-09 21:21:51.294+09:00"
            },
            {
                "clientID": "inception4_gqCCuU2tlCR8dYyx",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:12.390+09:00",
                "progress": 99.18,
                "stopTime": "2020-02-09 22:11:55.609+09:00"
            },
            {
                "clientID": "inception4_Kvh4JwHyRorMeexS",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:01.058+09:00",
                "progress": 99.59,
                "stopTime": "2020-02-09 22:19:09.573+09:00"
            },
            {
                "clientID": "video_fezrd4HLhPdbdVou",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:24.646+09:00",
                "progress": 98.48,
                "stopTime": "2020-02-09 21:46:20.622+09:00"
            },
            {
                "clientID": "resnet50_ODd3FvPaK1QSP40c",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:38.464+09:00",
                "progress": 97.56,
                "stopTime": "2020-02-09 21:32:44.317+09:00"
            },
            {
                "clientID": "video_QT6D3WADEYBH6X39",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:13.658+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:45:22.522+09:00"
            },
            {
                "clientID": "googlenet_hNTXN7Wq8eY7O45X",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:47.558+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:26:00.831+09:00"
            },
            {
                "clientID": "googlenet_7LGgZ4aDd64FDm2g",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:56.014+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:26:19.047+09:00"
            },
            {
                "clientID": "googlenet_8cZXPYF3DvGO4r25",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:13.808+09:00",
                "progress": 99.88,
                "stopTime": "2020-02-09 21:29:05.705+09:00"
            },
            {
                "clientID": "chatbot_Yf3UDO7ACp9yAfU7",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:01.917+09:00",
                "progress": 99.25,
                "stopTime": "2020-02-09 21:16:44.818+09:00"
            },
            {
                "clientID": "inception4_9HHDgp6XF3yYOOTU",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:38.744+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:34:13.916+09:00"
            },
            {
                "clientID": "resnet50_rwnTUi3kmsIbi2RQ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:35.192+09:00",
                "progress": 99.74,
                "stopTime": "2020-02-09 21:34:43.940+09:00"
            },
            {
                "clientID": "chatbot_yBFU2mI4FqboDWw4",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:04.790+09:00",
                "progress": 99.9,
                "stopTime": "2020-02-09 21:16:28.884+09:00"
            },
            {
                "clientID": "inception4_eyFRg72hSMPpan2J",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:01.402+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:05:57.352+09:00"
            },
            {
                "clientID": "dcgan_pVxRdMUOBOmZBsKi",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:49.743+09:00",
                "progress": 50.0,
                "stopTime": "2020-02-09 21:17:41.223+09:00"
            },
            {
                "clientID": "dcgan_70jnOANU5Gjn4eO7",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:42.907+09:00",
                "progress": 99.84,
                "stopTime": "2020-02-09 21:22:49.508+09:00"
            },
            {
                "clientID": "video_GMBG6VaFimna8Glu",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:49.105+09:00",
                "progress": 90.9,
                "stopTime": "2020-02-09 21:45:33.037+09:00"
            },
            {
                "clientID": "vgg16_Cp7lCzte3rTMc9nH",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:45.010+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:49:42.172+09:00"
            },
            {
                "clientID": "video_eJVemiCZ7hdmyOmk",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:17.751+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:45:03.636+09:00"
            },
            {
                "clientID": "chatbot_W7kndN5gTODMdFXr",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:35.570+09:00",
                "progress": 99.62,
                "stopTime": "2020-02-09 21:18:37.377+09:00"
            },
            {
                "clientID": "googlenet_VYFNmQyCPzbL1gCK",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:26.754+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:26:58.027+09:00"
            },
            {
                "clientID": "chatbot_9kjeSQ99Tz8waknm",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:02.308+09:00",
                "progress": 99.28,
                "stopTime": "2020-02-09 21:16:07.997+09:00"
            },
            {
                "clientID": "resnet50_mKKDsJXqZ46xAKo1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:21.155+09:00",
                "progress": 99.78,
                "stopTime": "2020-02-09 21:42:00.988+09:00"
            },
            {
                "clientID": "chatbot_8fjqnFKd0pbyTWsU",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:04.628+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:04.906+09:00"
            },
            {
                "clientID": "resnet50_qsI41WpCCb2l6Jby",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:35.686+09:00",
                "progress": 99.88,
                "stopTime": "2020-02-09 21:43:01.390+09:00"
            },
            {
                "clientID": "chatbot_qLTbaxzAipGqNAAv",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:35.076+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:17:17.046+09:00"
            },
            {
                "clientID": "vgg16_U9s3jKQlzTsL9bNz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:27.848+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:43.689+09:00"
            },
            {
                "clientID": "video_Il68TKN16khn4Yce",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:30.296+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:42:13.327+09:00"
            },
            {
                "clientID": "video_S1nCS9anPxxRVWMn",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:51.062+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:46:35.361+09:00"
            },
            {
                "clientID": "resnet50_SyKMmnpTUIwbnb8f",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:30.137+09:00",
                "progress": 99.86,
                "stopTime": "2020-02-09 21:39:13.412+09:00"
            },
            {
                "clientID": "video_5HBvHGl2RMJ0CyvN",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:25.033+09:00",
                "progress": 99.27,
                "stopTime": "2020-02-09 21:45:20.406+09:00"
            },
            {
                "clientID": "chatbot_rL2CR7vHyvwyqDqK",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:05.138+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:02.493+09:00"
            },
            {
                "clientID": "dcgan_wGGeNQt0OfVXjCk5",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:49.385+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:24:38.233+09:00"
            },
            {
                "clientID": "dcgan_UJ7Bb7lUBqhsNyxO",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:30.882+09:00",
                "progress": 99.84,
                "stopTime": "2020-02-09 21:26:11.334+09:00"
            },
            {
                "clientID": "video_EXdMOpVVtpKfu4Fi",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:14.504+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:44:14.522+09:00"
            },
            {
                "clientID": "resnet50_Hbuy8juqp0lCZVKc",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:57.270+09:00",
                "progress": 99.84,
                "stopTime": "2020-02-09 21:37:54.406+09:00"
            },
            {
                "clientID": "resnet50_vSfKHLFo4UgmcoUl",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:27.073+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:42.031+09:00"
            },
            {
                "clientID": "resnet50_JZk9VjtUuv6CgwG6",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:56.270+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:03.041+09:00"
            },
            {
                "clientID": "googlenet_ojzA4jsnYC2wIxPY",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:02.987+09:00",
                "progress": 99.3,
                "stopTime": "2020-02-09 21:26:23.105+09:00"
            },
            {
                "clientID": "resnet50_BwailsOuLrHj9SWy",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:38.515+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:32:39.437+09:00"
            },
            {
                "clientID": "dcgan_vQDzj9Unn3T6ae3m",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:00.769+09:00",
                "progress": 99.65,
                "stopTime": "2020-02-09 21:19:23.556+09:00"
            },
            {
                "clientID": "video_BVKJmAvOPS6MVa2a",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:21.310+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:45:26.148+09:00"
            },
            {
                "clientID": "chatbot_7vgfjOuHRkxdW20C",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:35.397+09:00",
                "progress": 99.46,
                "stopTime": "2020-02-09 21:15:59.875+09:00"
            },
            {
                "clientID": "inception4_nN7AApHVpPN274to",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:24.360+09:00",
                "progress": 99.36,
                "stopTime": "2020-02-09 22:15:23.830+09:00"
            },
            {
                "clientID": "inception4_3TPvXKfnjFGLrd2K",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:39.470+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:35:27.646+09:00"
            },
            {
                "clientID": "video_l62b1CRP49i7K3Q3",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:22.742+09:00",
                "progress": 99.23,
                "stopTime": "2020-02-09 21:42:53.847+09:00"
            },
            {
                "clientID": "resnet50_oc84WAp0wUWyIlVS",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:43.076+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:23.964+09:00"
            },
            {
                "clientID": "resnet50_gj4RtdzsHGKl0CZI",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:31.321+09:00",
                "progress": 99.89,
                "stopTime": "2020-02-09 21:43:09.718+09:00"
            },
            {
                "clientID": "video_CusZJ7eZol7yEi3K",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:16.354+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:42:43.406+09:00"
            },
            {
                "clientID": "chatbot_C7gkhZAK6HaSQwv2",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:04.383+09:00",
                "progress": 99.23,
                "stopTime": "2020-02-09 21:17:03.327+09:00"
            },
            {
                "clientID": "chatbot_gIkMPImqkyVx8uVo",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:09.791+09:00",
                "progress": 99.3,
                "stopTime": "2020-02-09 21:15:44.443+09:00"
            },
            {
                "clientID": "inception4_orZ35SWt74Iv8fX2",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:06.162+09:00",
                "progress": 99.52,
                "stopTime": "2020-02-09 22:19:27.276+09:00"
            },
            {
                "clientID": "dcgan_1VnH5WnU52e7hZoX",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:12.436+09:00",
                "progress": -1,
                "stopTime": "2020-02-09 21:17:50.771+09:00"
            },
            {
                "clientID": "vgg16_CTRSfzXdVLS941Rz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:02.176+09:00",
                "progress": 99.19,
                "stopTime": "2020-02-09 21:54:02.037+09:00"
            },
            {
                "clientID": "vgg16_IWsTsp4YSBtBeTZg",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:31.171+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:59:39.714+09:00"
            },
            {
                "clientID": "chatbot_dEj46Z0LjOnkzj75",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:49.396+09:00",
                "progress": 99.11,
                "stopTime": "2020-02-09 21:16:15.357+09:00"
            },
            {
                "clientID": "video_NR9HaW0Z4joysOXd",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:55.650+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:40:27.597+09:00"
            },
            {
                "clientID": "vgg16_NqPG0kFSp58rH3h7",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:48.860+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:49:55.613+09:00"
            },
            {
                "clientID": "resnet50_VFdC9rF0k25iGwTo",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:16.642+09:00",
                "progress": 99.62,
                "stopTime": "2020-02-09 21:35:32.781+09:00"
            },
            {
                "clientID": "googlenet_oJ4ZM8kAzgcvb09K",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:02.121+09:00",
                "progress": 99.75,
                "stopTime": "2020-02-09 21:29:48.628+09:00"
            },
            {
                "clientID": "chatbot_VOCHMKG3w4BqrF36",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:44.854+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:15:34.503+09:00"
            },
            {
                "clientID": "video_r05TUqZIZdL2uL6C",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:53.303+09:00",
                "progress": 99.67,
                "stopTime": "2020-02-09 21:43:54.757+09:00"
            },
            {
                "clientID": "chatbot_Tc5yCvRZYWlsEueP",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:03.434+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:15:53.922+09:00"
            },
            {
                "clientID": "vgg16_EkQgnkSGkCHIZTqx",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:32.888+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:50:23.822+09:00"
            },
            {
                "clientID": "vgg16_IpaUBh6MBdGKJCpW",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:29.976+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 22:00:04.630+09:00"
            },
            {
                "clientID": "vgg16_P3yqXv09fhCJKiQy",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:33.852+09:00",
                "progress": 95.23,
                "stopTime": "2020-02-09 21:49:25.099+09:00"
            },
            {
                "clientID": "inception4_e96smJYaNa68YfOl",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:03.555+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:06:06.605+09:00"
            },
            {
                "clientID": "video_mR5r3orX783mvC4h",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:20.908+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:46:32.975+09:00"
            },
            {
                "clientID": "googlenet_yOyfREy829hhImGg",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:35.593+09:00",
                "progress": 99.91,
                "stopTime": "2020-02-09 21:34:29.919+09:00"
            },
            {
                "clientID": "googlenet_crJ6FTSXCIkoO1GG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:38.374+09:00",
                "progress": 92.59,
                "stopTime": "2020-02-09 21:26:09.667+09:00"
            },
            {
                "clientID": "vgg16_Dx7oZDUIZ9ehq9sj",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:49.128+09:00",
                "progress": 200.0,
                "stopTime": "2020-02-09 21:50:13.481+09:00"
            },
            {
                "clientID": "chatbot_JDdR2133fqtwuveS",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:13.913+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:11.398+09:00"
            },
            {
                "clientID": "inception4_QusYPNHl69mhHy1R",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:39.270+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:32:23.956+09:00"
            },
            {
                "clientID": "googlenet_XAtj13kzyXSXgfea",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:17.246+09:00",
                "progress": 99.41,
                "stopTime": "2020-02-09 21:28:04.228+09:00"
            },
            {
                "clientID": "vgg16_8R3GAbznZDQ1rs03",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:51.892+09:00",
                "progress": 98.76,
                "stopTime": "2020-02-09 21:51:08.608+09:00"
            },
            {
                "clientID": "chatbot_S0aHX6ZEe7VRRY7L",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:21.588+09:00",
                "progress": 99.87,
                "stopTime": "2020-02-09 21:17:13.638+09:00"
            },
            {
                "clientID": "chatbot_fceVEuyF7Bkev8Wk",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:27.927+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:16:32.934+09:00"
            },
            {
                "clientID": "resnet50_DeSfTJ3xBeoJSHNW",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:00.749+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:13.680+09:00"
            },
            {
                "clientID": "video_XWSaaqxjDhp4jasq",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:40.322+09:00",
                "progress": 99.75,
                "stopTime": "2020-02-09 21:43:45.024+09:00"
            },
            {
                "clientID": "video_eScbDua3lNNHuQ0W",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:28.866+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:45:44.091+09:00"
            },
            {
                "clientID": "dcgan_aQwL2H4jkPWfp1CG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:30.018+09:00",
                "progress": 99.92,
                "stopTime": "2020-02-09 21:23:08.643+09:00"
            },
            {
                "clientID": "inception4_adVdasEhfm4iovzm",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:51.868+09:00",
                "progress": 99.71,
                "stopTime": "2020-02-09 22:29:04.102+09:00"
            },
            {
                "clientID": "vgg16_kyRIhjVxwuLG4jLc",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:49.120+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:08.609+09:00"
            },
            {
                "clientID": "googlenet_ppsPEMRZ4KOul5Bv",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:36.282+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 21:28:16.159+09:00"
            },
            {
                "clientID": "chatbot_xb1nMTNc1CB3Iz7S",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:01.118+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:15:32.220+09:00"
            },
            {
                "clientID": "googlenet_oozLIaEMiLMO77QQ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:41.833+09:00",
                "progress": 50.0,
                "stopTime": "2020-02-09 21:26:00.105+09:00"
            },
            {
                "clientID": "inception4_PdMdUg9o4tIJdwSH",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:53.367+09:00",
                "progress": 99.54,
                "stopTime": "2020-02-09 22:14:12.976+09:00"
            },
            {
                "clientID": "dcgan_AGGgislT3yA7yu50",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:28.986+09:00",
                "progress": 99.64,
                "stopTime": "2020-02-09 21:25:40.967+09:00"
            },
            {
                "clientID": "video_RPYLhBu4Vc3woARO",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:25.056+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:47:44.538+09:00"
            },
            {
                "clientID": "vgg16_VETB0FkXeJQOeVbE",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:12:45.125+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:58:43.422+09:00"
            },
            {
                "clientID": "video_PXaI3QdjSZMOMPYB",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:55.040+09:00",
                "progress": 99.58,
                "stopTime": "2020-02-09 21:48:05.348+09:00"
            },
            {
                "clientID": "dcgan_K5WL4NRe0LYoKdJa",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:31.333+09:00",
                "progress": 99.41,
                "stopTime": "2020-02-09 21:19:12.010+09:00"
            },
            {
                "clientID": "dcgan_LtNaDWLyWpYnYSbj",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:21.249+09:00",
                "progress": 99.75,
                "stopTime": "2020-02-09 21:23:57.985+09:00"
            },
            {
                "clientID": "resnet50_egzIPtUn8twSsGsI",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:24.827+09:00",
                "progress": 99.64,
                "stopTime": "2020-02-09 21:35:28.263+09:00"
            },
            {
                "clientID": "inception4_WuMmS4577duEhaeO",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:05.439+09:00",
                "progress": 99.59,
                "stopTime": "2020-02-09 22:15:19.403+09:00"
            },
            {
                "clientID": "video_f8R36T0hyBZptn2s",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:21.428+09:00",
                "progress": 98.69,
                "stopTime": "2020-02-09 21:43:51.436+09:00"
            },
            {
                "clientID": "inception4_1PUGhsHhnFp5whsS",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:13.674+09:00",
                "progress": 99.68,
                "stopTime": "2020-02-09 22:22:57.056+09:00"
            },
            {
                "clientID": "resnet50_mLMpJabkUEiQPYRe",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:54.483+09:00",
                "progress": 99.82,
                "stopTime": "2020-02-09 21:36:08.321+09:00"
            },
            {
                "clientID": "resnet50_4IF5gdnrflPnT2rj",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:25.814+09:00",
                "progress": 98.95,
                "stopTime": "2020-02-09 21:34:13.598+09:00"
            },
            {
                "clientID": "inception4_lPtqFXnNYRyEAuUG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:08.495+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:06:46.834+09:00"
            },
            {
                "clientID": "vgg16_3tpTstq6jC3NVvb9",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:35.510+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:59:54.655+09:00"
            },
            {
                "clientID": "chatbot_FHFgbPYu5OtHHdoQ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:43.152+09:00",
                "progress": 90.0,
                "stopTime": "2020-02-09 21:15:34.125+09:00"
            },
            {
                "clientID": "inception4_l9ie1JYiu085ST8j",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:36.585+09:00",
                "progress": 98.36,
                "stopTime": "2020-02-09 22:07:39.410+09:00"
            },
            {
                "clientID": "inception4_Zv4N5VospvYLgw35",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:13.012+09:00",
                "progress": 99.39,
                "stopTime": "2020-02-09 22:16:42.442+09:00"
            },
            {
                "clientID": "googlenet_jtzaOBuVWIVcsCkY",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:06.193+09:00",
                "progress": 99.55,
                "stopTime": "2020-02-09 21:26:02.968+09:00"
            },
            {
                "clientID": "vgg16_FVHIyCKJoUq82pgl",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:49.115+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:18.549+09:00"
            },
            {
                "clientID": "dcgan_Gcb3ViHHkYKZMssr",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:01.703+09:00",
                "progress": 99.71,
                "stopTime": "2020-02-09 21:20:25.492+09:00"
            },
            {
                "clientID": "video_1J4B2QG5sOPocknp",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:30.856+09:00",
                "progress": 98.47,
                "stopTime": "2020-02-09 21:47:14.462+09:00"
            },
            {
                "clientID": "video_KzQODPfrkNLOcfK1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:53.790+09:00",
                "progress": 99.74,
                "stopTime": "2020-02-09 21:44:57.796+09:00"
            },
            {
                "clientID": "dcgan_rWA6uytgXMX0gool",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:07.108+09:00",
                "progress": 50.0,
                "stopTime": "2020-02-09 21:17:54.673+09:00"
            },
            {
                "clientID": "inception4_bZJVC7utSCnz4u5D",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:45.370+09:00",
                "progress": 94.73,
                "stopTime": "2020-02-09 22:03:31.018+09:00"
            },
            {
                "clientID": "chatbot_2c6eo2A8wQB0LTxz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:13.725+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:24.799+09:00"
            },
            {
                "clientID": "googlenet_ehSBMbk4Xo7plIH9",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:33.083+09:00",
                "progress": 99.73,
                "stopTime": "2020-02-09 21:28:14.778+09:00"
            },
            {
                "clientID": "video_EcYXVtL4G08C0x33",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:28.877+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:46:44.354+09:00"
            },
            {
                "clientID": "dcgan_UqVGqI7I3hgWxdii",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:34.560+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:17:18.906+09:00"
            },
            {
                "clientID": "chatbot_iR6pFCs2sLVxGUF4",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:51.637+09:00",
                "progress": 97.81,
                "stopTime": "2020-02-09 21:15:44.444+09:00"
            },
            {
                "clientID": "chatbot_nftkEoAfHb0YjUeH",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:15.479+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:36.606+09:00"
            },
            {
                "clientID": "chatbot_VPUlFAXVVuBT1hjG",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:39.532+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:17:42.808+09:00"
            },
            {
                "clientID": "vgg16_Vs3L0wyCMoMivV6g",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:29.717+09:00",
                "progress": 99.5,
                "stopTime": "2020-02-09 21:57:01.463+09:00"
            },
            {
                "clientID": "inception4_g3Tji7aDNnWa9JOo",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:33.289+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:32:19.131+09:00"
            },
            {
                "clientID": "resnet50_ISW9mbkyG25wPgZo",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:12.407+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:42.417+09:00"
            },
            {
                "clientID": "dcgan_R6XiEjMC6ZNbZaSb",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:56.031+09:00",
                "progress": 99.47,
                "stopTime": "2020-02-09 21:22:15.120+09:00"
            },
            {
                "clientID": "inception4_oCmWG6KDDrL7T6RI",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:25.683+09:00",
                "progress": 99.21,
                "stopTime": "2020-02-09 22:12:34.791+09:00"
            },
            {
                "clientID": "dcgan_6VRXAjCgf6kPdieW",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:31.424+09:00",
                "progress": 98.67,
                "stopTime": "2020-02-09 21:19:07.904+09:00"
            },
            {
                "clientID": "resnet50_sYRJjja1CUAFnaVw",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:19.963+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:53.064+09:00"
            },
            {
                "clientID": "googlenet_ZjOsW1bPb9gHiQkP",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:01.953+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:33:21.327+09:00"
            },
            {
                "clientID": "resnet50_YnPV7wsagzeBaDxI",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:17.300+09:00",
                "progress": 99.58,
                "stopTime": "2020-02-09 21:35:17.985+09:00"
            },
            {
                "clientID": "inception4_1BK3hD8Rt3x7nsJe",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:18.096+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:07:56.051+09:00"
            },
            {
                "clientID": "vgg16_TZ7IyRzaDggn9yJ2",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:54.518+09:00",
                "progress": 99.62,
                "stopTime": "2020-02-09 21:59:30.825+09:00"
            },
            {
                "clientID": "inception4_7KD0qAlMxn8iNVno",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:57.590+09:00",
                "progress": 99.59,
                "stopTime": "2020-02-09 22:16:43.261+09:00"
            },
            {
                "clientID": "googlenet_17UwR00HMgEYhhqc",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:16.520+09:00",
                "progress": 99.84,
                "stopTime": "2020-02-09 21:26:44.135+09:00"
            },
            {
                "clientID": "chatbot_HxaVJz5DoYSChHQB",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:53.701+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:15:31.320+09:00"
            },
            {
                "clientID": "vgg16_vMWe4nLCiZGhaVfo",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:57.956+09:00",
                "progress": 99.21,
                "stopTime": "2020-02-09 21:53:16.300+09:00"
            },
            {
                "clientID": "video_LxfiWJdhIBuodQhy",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:29:19.345+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:30:34.717+09:00"
            },
            {
                "clientID": "googlenet_Wn8M5ngEDf9jw0zd",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:12.185+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:26:46.658+09:00"
            },
            {
                "clientID": "video_UkrR61v6j0mlhe7a",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:41.755+09:00",
                "progress": 99.58,
                "stopTime": "2020-02-09 21:46:55.793+09:00"
            },
            {
                "clientID": "inception4_J3CFk0TFGNqKfFYd",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:26.117+09:00",
                "progress": 99.33,
                "stopTime": "2020-02-09 22:16:06.783+09:00"
            },
            {
                "clientID": "video_BTxRB3E3QxhRItc5",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:23.857+09:00",
                "progress": 99.68,
                "stopTime": "2020-02-09 21:41:17.726+09:00"
            },
            {
                "clientID": "googlenet_du12agGe7lUrI0wz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:10.511+09:00",
                "progress": 99.86,
                "stopTime": "2020-02-09 21:26:47.014+09:00"
            },
            {
                "clientID": "resnet50_XKYxDGeO3eRtad0w",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:42.020+09:00",
                "progress": 98.9,
                "stopTime": "2020-02-09 21:34:27.504+09:00"
            },
            {
                "clientID": "vgg16_DmNL29ioT7C050Ln",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:51.928+09:00",
                "progress": 99.62,
                "stopTime": "2020-02-09 21:58:23.670+09:00"
            },
            {
                "clientID": "video_zCYGqBKShLJux0x5",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:10.180+09:00",
                "progress": 99.27,
                "stopTime": "2020-02-09 21:41:21.317+09:00"
            },
            {
                "clientID": "video_94cLfjGz8bba562V",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:20.188+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:45:28.711+09:00"
            },
            {
                "clientID": "vgg16_1mgH3gubrosaeBf1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:07.770+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:41.146+09:00"
            },
            {
                "clientID": "resnet50_kACJR4ZQy9aZdDlx",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:00.344+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:09.114+09:00"
            },
            {
                "clientID": "resnet50_kZQzEGqrh79QG8a6",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:42.609+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:33:58.558+09:00"
            },
            {
                "clientID": "resnet50_9dpFEvWsMnCTs9o9",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:16.175+09:00",
                "progress": 99.29,
                "stopTime": "2020-02-09 21:34:51.998+09:00"
            },
            {
                "clientID": "inception4_YXpQJf7U4QY6tuCi",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:39.160+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:35:08.874+09:00"
            },
            {
                "clientID": "resnet50_hobA097FePEvn5VC",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:50.429+09:00",
                "progress": 99.8,
                "stopTime": "2020-02-09 21:36:28.332+09:00"
            },
            {
                "clientID": "vgg16_VOdxi8BczHylKWDM",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:33.301+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:48:28.352+09:00"
            },
            {
                "clientID": "chatbot_sLTVY47L9kMAuNo2",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:10.250+09:00",
                "progress": 99.75,
                "stopTime": "2020-02-09 21:17:00.182+09:00"
            },
            {
                "clientID": "vgg16_BZSNlAcs8fEipj0C",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:48.704+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:49:57.946+09:00"
            },
            {
                "clientID": "vgg16_mL1EaqxGlr3JRCr7",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:14.510+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:59:28.221+09:00"
            },
            {
                "clientID": "chatbot_AdcRr3hierWBg3Of",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:15.143+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:17:04.862+09:00"
            },
            {
                "clientID": "resnet50_aQUUncXrW5aCil3y",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:06.162+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:22.800+09:00"
            },
            {
                "clientID": "resnet50_T6RmuvEUNbmXczUs",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:36.469+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:34:43.651+09:00"
            },
            {
                "clientID": "dcgan_P72kKxPQ0IFc4DJl",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:09.812+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:21:32.991+09:00"
            },
            {
                "clientID": "googlenet_0YQxhNGA8dBZpgtH",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:16.821+09:00",
                "progress": 99.33,
                "stopTime": "2020-02-09 21:28:24.375+09:00"
            },
            {
                "clientID": "inception4_FlC8KEvaYAKPIDZq",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:19.363+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:08:20.841+09:00"
            },
            {
                "clientID": "chatbot_CsnM0zAE98qybTdW",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:19.313+09:00",
                "progress": 99.6,
                "stopTime": "2020-02-09 21:16:11.495+09:00"
            },
            {
                "clientID": "googlenet_ZFxJqSS6YfXa8Era",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:52.252+09:00",
                "progress": 99.84,
                "stopTime": "2020-02-09 21:25:43.291+09:00"
            },
            {
                "clientID": "googlenet_KGwRyRZVrcdlPBHD",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:31.015+09:00",
                "progress": 99.83,
                "stopTime": "2020-02-09 21:34:03.174+09:00"
            },
            {
                "clientID": "chatbot_9gaz9mXofrq2Rk0c",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:08.000+09:00",
                "progress": 99.7,
                "stopTime": "2020-02-09 21:16:16.812+09:00"
            },
            {
                "clientID": "chatbot_GWfldr3OLEIs6oJg",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:25.792+09:00",
                "progress": 98.63,
                "stopTime": "2020-02-09 21:16:20.990+09:00"
            },
            {
                "clientID": "resnet50_sIqCuL9TxJoreK3T",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:41.805+09:00",
                "progress": 90.0,
                "stopTime": "2020-02-09 21:32:55.811+09:00"
            },
            {
                "clientID": "chatbot_LhlG3ESvaRYfNbmD",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:04.372+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:13.008+09:00"
            },
            {
                "clientID": "inception4_TowBhY1nNuW2mto2",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:55.927+09:00",
                "progress": 99.73,
                "stopTime": "2020-02-09 22:33:30.409+09:00"
            },
            {
                "clientID": "chatbot_tJW5dZHpScXXtpli",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:25.575+09:00",
                "progress": 98.03,
                "stopTime": "2020-02-09 21:16:45.895+09:00"
            },
            {
                "clientID": "chatbot_oiok8ob91xJRmQdz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:17.093+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:36.971+09:00"
            },
            {
                "clientID": "vgg16_jiE6x41H597AnkP1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:25.620+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:59:30.732+09:00"
            },
            {
                "clientID": "dcgan_qY0XLI3bvAWqh6iC",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:28.917+09:00",
                "progress": 99.69,
                "stopTime": "2020-02-09 21:25:30.401+09:00"
            },
            {
                "clientID": "googlenet_SDuLXSDivwBcGrSA",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:39.257+09:00",
                "progress": 96.29,
                "stopTime": "2020-02-09 21:26:55.754+09:00"
            },
            {
                "clientID": "inception4_9AwfwKLddnXh2EWk",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:16.825+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:07:30.368+09:00"
            },
            {
                "clientID": "dcgan_etDthJntUPFSbySG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:20.436+09:00",
                "progress": 99.59,
                "stopTime": "2020-02-09 21:19:29.785+09:00"
            },
            {
                "clientID": "chatbot_VCdcIojp8HpE0oA1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:44.889+09:00",
                "progress": 99.8,
                "stopTime": "2020-02-09 21:18:09.549+09:00"
            },
            {
                "clientID": "googlenet_1yBzfCuaYElVeKdb",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:10.780+09:00",
                "progress": 50.0,
                "stopTime": "2020-02-09 21:27:13.873+09:00"
            },
            {
                "clientID": "video_C7niP1VEUlRDyvMF",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:54.084+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:50:12.055+09:00"
            },
            {
                "clientID": "inception4_XHwGY7tLCWeZZ4Qt",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:57.459+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:32:42.340+09:00"
            },
            {
                "clientID": "googlenet_m9W7DXy5CsSt8cE0",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:51.555+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:33:01.336+09:00"
            },
            {
                "clientID": "inception4_3Ey15Blj8I1eaFRt",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:20.619+09:00",
                "progress": 99.68,
                "stopTime": "2020-02-09 22:23:05.657+09:00"
            },
            {
                "clientID": "resnet50_nKaa6rgQHaJaa2Ja",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:11.193+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:22.797+09:00"
            },
            {
                "clientID": "googlenet_QMniq3Dj5x3pMHtW",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:27.834+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:26:57.338+09:00"
            },
            {
                "clientID": "inception4_5067wOaiXp45mYxL",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:39.083+09:00",
                "progress": 98.24,
                "stopTime": "2020-02-09 22:06:28.310+09:00"
            },
            {
                "clientID": "dcgan_b81d4zpRVoge3tUd",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:12:51.331+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:24:59.887+09:00"
            },
            {
                "clientID": "vgg16_YBfVnyu2vfEQJmOI",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:49.146+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:22.848+09:00"
            },
            {
                "clientID": "vgg16_XQXnCATfYCuuVcKF",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:00.239+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:25.666+09:00"
            },
            {
                "clientID": "dcgan_f5JYvjOjxAgrvBin",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:44.613+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:23:53.691+09:00"
            },
            {
                "clientID": "inception4_EeXW45VzOxkIYwzg",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:06.755+09:00",
                "progress": 99.58,
                "stopTime": "2020-02-09 22:21:30.162+09:00"
            },
            {
                "clientID": "googlenet_Eb2DvkHYzQx61LWM",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:42.208+09:00",
                "progress": 99.82,
                "stopTime": "2020-02-09 21:26:59.605+09:00"
            },
            {
                "clientID": "chatbot_EbkxSiaP8EHHJ1Kz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:01.764+09:00",
                "progress": 97.83,
                "stopTime": "2020-02-09 21:15:38.407+09:00"
            },
            {
                "clientID": "vgg16_BWA5iyTHOO78raVY",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:12:57.326+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:54:07.958+09:00"
            },
            {
                "clientID": "inception4_FSPDVxzr4p4jtRWW",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:14.209+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:08:22.651+09:00"
            },
            {
                "clientID": "video_VwcQJTt8dFarNBYG",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:45.093+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:45:06.372+09:00"
            },
            {
                "clientID": "video_RYDAlDJY2jMcAhEH",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:18.139+09:00",
                "progress": 98.85,
                "stopTime": "2020-02-09 21:43:25.455+09:00"
            },
            {
                "clientID": "vgg16_3gPWx89xoIVtbihi",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:36.752+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:48:57.539+09:00"
            },
            {
                "clientID": "inception4_ShJ19CETLNURYBlC",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:55.543+09:00",
                "progress": 99.11,
                "stopTime": "2020-02-09 22:03:12.234+09:00"
            },
            {
                "clientID": "vgg16_ggj89mCV7iy5nyRG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:43.087+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:49:23.933+09:00"
            },
            {
                "clientID": "chatbot_eUkhRzYP4Aomg8On",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:06.097+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:16:11.110+09:00"
            },
            {
                "clientID": "video_1xcGKbl23TxFcO7n",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:16.398+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:47:10.185+09:00"
            },
            {
                "clientID": "googlenet_XyJV2SPhLgLU2AcM",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:07.858+09:00",
                "progress": 99.83,
                "stopTime": "2020-02-09 21:33:33.150+09:00"
            },
            {
                "clientID": "vgg16_YzhLDznZF2zqP3l2",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:27.182+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:36.615+09:00"
            },
            {
                "clientID": "video_1bYOLPAPfyJcHaEx",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:23.725+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:46:17.169+09:00"
            },
            {
                "clientID": "resnet50_jEGNDZ3ShUQFr6EO",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:51.661+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:33:05.456+09:00"
            },
            {
                "clientID": "googlenet_ngttPxvdQMMUq3wt",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:30.774+09:00",
                "progress": 99.87,
                "stopTime": "2020-02-09 21:33:32.714+09:00"
            },
            {
                "clientID": "googlenet_dkV0QwenPZMmUlGF",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:38.109+09:00",
                "progress": 96.4,
                "stopTime": "2020-02-09 21:27:20.111+09:00"
            },
            {
                "clientID": "googlenet_D0jVyFp5IMrymdoi",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:51.400+09:00",
                "progress": 99.95,
                "stopTime": "2020-02-09 21:31:47.834+09:00"
            },
            {
                "clientID": "googlenet_5jxFJxZSW7fpWPZZ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:06.632+09:00",
                "progress": 99.55,
                "stopTime": "2020-02-09 21:29:00.501+09:00"
            },
            {
                "clientID": "video_IKWseO9QEBdUXqxz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:24.892+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:46:25.105+09:00"
            },
            {
                "clientID": "video_hmntYcia0hKsXpH3",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:32.086+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:46:41.205+09:00"
            },
            {
                "clientID": "googlenet_zfP9tnieabSUiHqN",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:41.756+09:00",
                "progress": 88.23,
                "stopTime": "2020-02-09 21:26:10.370+09:00"
            },
            {
                "clientID": "vgg16_SlD5YRqgQBd5Gt0W",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:58.555+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:25.681+09:00"
            },
            {
                "clientID": "googlenet_LL9tLgxud2tnLdvi",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:51.895+09:00",
                "progress": 99.54,
                "stopTime": "2020-02-09 21:25:29.469+09:00"
            },
            {
                "clientID": "vgg16_fh0j3b1Bhu14CD7M",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:29.703+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 22:00:16.164+09:00"
            },
            {
                "clientID": "googlenet_VTVie5Ca4kbx1DPq",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:51.678+09:00",
                "progress": 99.73,
                "stopTime": "2020-02-09 21:29:38.282+09:00"
            },
            {
                "clientID": "vgg16_B9zOCB6Gy5WNw4u1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:19.147+09:00",
                "progress": 98.48,
                "stopTime": "2020-02-09 21:50:58.390+09:00"
            },
            {
                "clientID": "chatbot_ci6troNnCLYOJfID",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:03.436+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:15:47.357+09:00"
            },
            {
                "clientID": "inception4_JGPQlXVFZrG2rdSj",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:23.580+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:33:45.752+09:00"
            },
            {
                "clientID": "googlenet_9BKHj6td2S62aAtT",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:57.884+09:00",
                "progress": 75.0,
                "stopTime": "2020-02-09 21:26:29.420+09:00"
            },
            {
                "clientID": "dcgan_u0juGXdhYH1zWMUg",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:32.383+09:00",
                "progress": 99.62,
                "stopTime": "2020-02-09 21:22:34.978+09:00"
            },
            {
                "clientID": "chatbot_8S32icYBYQ8G2Wtu",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:56.505+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:15:32.636+09:00"
            },
            {
                "clientID": "googlenet_qK6QImXqbzbAzekT",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:09.176+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 21:27:14.110+09:00"
            },
            {
                "clientID": "inception4_ovh8XQHyzZG1h75S",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:41.182+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 22:18:33.714+09:00"
            },
            {
                "clientID": "video_xAPwXdfRqkRAKHR4",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:21.479+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:45:03.633+09:00"
            },
            {
                "clientID": "dcgan_v4MR4BGNkWQpSazn",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:33.770+09:00",
                "progress": 85.71,
                "stopTime": "2020-02-09 21:17:29.822+09:00"
            },
            {
                "clientID": "chatbot_dBHOvig2prKZJrAG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:55.674+09:00",
                "progress": 99.06,
                "stopTime": "2020-02-09 21:17:15.360+09:00"
            },
            {
                "clientID": "vgg16_pqsWnyTNr3SJFixZ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:27.809+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:44.988+09:00"
            },
            {
                "clientID": "video_vfnF4I39D4e5OIQq",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:49.747+09:00",
                "progress": 99.55,
                "stopTime": "2020-02-09 21:46:21.922+09:00"
            },
            {
                "clientID": "chatbot_Nk4PfLawT7L2dH0o",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:16.566+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:17:20.557+09:00"
            },
            {
                "clientID": "inception4_Bt98uMQfJL0D5KJL",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:52.219+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 22:19:11.156+09:00"
            },
            {
                "clientID": "inception4_Y7JGykypgU97SNd5",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:39.037+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 22:34:11.495+09:00"
            },
            {
                "clientID": "video_kmIMI0T9yEyjrEbN",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:47.067+09:00",
                "progress": 99.65,
                "stopTime": "2020-02-09 21:43:47.138+09:00"
            },
            {
                "clientID": "dcgan_MJQIx2q62yVPJTpW",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:45.022+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:17:36.233+09:00"
            },
            {
                "clientID": "inception4_687JQMr1qlQyuGov",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:16.745+09:00",
                "progress": 99.62,
                "stopTime": "2020-02-09 22:26:05.717+09:00"
            },
            {
                "clientID": "googlenet_2NsIgSp58kwIfef1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:38.427+09:00",
                "progress": 98.09,
                "stopTime": "2020-02-09 21:26:39.035+09:00"
            },
            {
                "clientID": "inception4_dnT5Q9xbtKqns7bC",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:19.726+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:08:11.083+09:00"
            },
            {
                "clientID": "googlenet_ZSOqtSw4srneyowN",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:07.833+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:26:40.362+09:00"
            },
            {
                "clientID": "resnet50_dp5AVb5yFbY0lhvx",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:00.043+09:00",
                "progress": 99.8,
                "stopTime": "2020-02-09 21:35:55.986+09:00"
            },
            {
                "clientID": "video_JV2ZDeLBLtpSJhRV",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:29.014+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:46:03.164+09:00"
            },
            {
                "clientID": "vgg16_CDEGfhSVkBNPVpc6",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:16.381+09:00",
                "progress": 98.87,
                "stopTime": "2020-02-09 21:52:09.797+09:00"
            },
            {
                "clientID": "chatbot_EqOXr3GZAMHB0WWE",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:36.831+09:00",
                "progress": 98.35,
                "stopTime": "2020-02-09 21:16:40.266+09:00"
            },
            {
                "clientID": "vgg16_UipEo6S1BhvTaJUS",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:29.986+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:59:49.776+09:00"
            },
            {
                "clientID": "video_AjrYuTCHYB9Q1Bva",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:26.023+09:00",
                "progress": 99.5,
                "stopTime": "2020-02-09 21:46:50.082+09:00"
            },
            {
                "clientID": "dcgan_775KPeoom3WZqfK7",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:55.696+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:25:05.776+09:00"
            },
            {
                "clientID": "video_BIBh4lXYL623IAMt",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:29.889+09:00",
                "progress": 99.71,
                "stopTime": "2020-02-09 21:42:15.871+09:00"
            },
            {
                "clientID": "dcgan_qG8LvXRo8obM56Gv",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:16.490+09:00",
                "progress": 99.91,
                "stopTime": "2020-02-09 21:21:41.443+09:00"
            },
            {
                "clientID": "vgg16_Ie10UY5XTnsAusUf",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:49.141+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:21.957+09:00"
            },
            {
                "clientID": "googlenet_alkKmWHEbEPN1auP",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:20.413+09:00",
                "progress": 99.72,
                "stopTime": "2020-02-09 21:28:20.405+09:00"
            },
            {
                "clientID": "video_Xzu3PC3hL21F0jvE",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:26.626+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:46:49.410+09:00"
            },
            {
                "clientID": "vgg16_kDjbYMXtP5zkFMrE",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:30.091+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:59:55.044+09:00"
            },
            {
                "clientID": "chatbot_PbRjM8BodzDMKNjw",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:25.249+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:18.850+09:00"
            },
            {
                "clientID": "dcgan_TvvvhtEifjjfdxJY",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:01.919+09:00",
                "progress": 99.22,
                "stopTime": "2020-02-09 21:19:34.757+09:00"
            },
            {
                "clientID": "vgg16_V2gjuIx87ZEpZsHW",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:26.029+09:00",
                "progress": 97.82,
                "stopTime": "2020-02-09 21:50:04.213+09:00"
            },
            {
                "clientID": "resnet50_SR3eAnIrAl2uBsGd",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:02.730+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:36:39.452+09:00"
            },
            {
                "clientID": "dcgan_JrillZUmfR3FeBPE",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:27.803+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:17:53.181+09:00"
            },
            {
                "clientID": "video_FT6fTaPJELL0EUAa",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:24.715+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:46:09.545+09:00"
            },
            {
                "clientID": "vgg16_zrX5ke666dwQoKyU",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:38.939+09:00",
                "progress": 99.33,
                "stopTime": "2020-02-09 21:54:10.390+09:00"
            },
            {
                "clientID": "video_EfWWXfOCkEXwHEU8",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:43.121+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:46:33.837+09:00"
            },
            {
                "clientID": "inception4_P0yePwK5f8zCFBjx",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:42.450+09:00",
                "progress": 97.29,
                "stopTime": "2020-02-09 22:04:49.485+09:00"
            },
            {
                "clientID": "chatbot_A7bAeMLMnnI7pBGF",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:35.645+09:00",
                "progress": 99.68,
                "stopTime": "2020-02-09 21:18:53.294+09:00"
            },
            {
                "clientID": "chatbot_3YZOSDyS4p94CFlG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:07.202+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:13.010+09:00"
            },
            {
                "clientID": "vgg16_LzkmMaeYQ6CvI6K0",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:04.725+09:00",
                "progress": 99.37,
                "stopTime": "2020-02-09 21:54:21.335+09:00"
            },
            {
                "clientID": "vgg16_dqjs5TqqVaClaKFz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:03.351+09:00",
                "progress": 98.61,
                "stopTime": "2020-02-09 21:51:20.344+09:00"
            },
            {
                "clientID": "vgg16_T2s6FrShf1tsxHaX",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:59.013+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:28.242+09:00"
            },
            {
                "clientID": "inception4_R1ghrOvcvS5BcXuq",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:48.011+09:00",
                "progress": 75.0,
                "stopTime": "2020-02-09 22:04:37.126+09:00"
            },
            {
                "clientID": "vgg16_bcVwLXZgqIfLJAaU",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:50.852+09:00",
                "progress": 99.35,
                "stopTime": "2020-02-09 21:54:48.866+09:00"
            },
            {
                "clientID": "vgg16_PFv8mlAZd6Tsa5Kf",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:31.432+09:00",
                "progress": 97.72,
                "stopTime": "2020-02-09 21:50:07.687+09:00"
            },
            {
                "clientID": "video_bdyOjCjMq1RqSnKr",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:45.244+09:00",
                "progress": 95.12,
                "stopTime": "2020-02-09 21:45:43.636+09:00"
            },
            {
                "clientID": "googlenet_ijsBx5kj4TAz8FxX",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:24.913+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:33:03.605+09:00"
            },
            {
                "clientID": "video_vBmkxzxZgS8smQWk",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:16.998+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:45:59.854+09:00"
            },
            {
                "clientID": "vgg16_43QWUNOhBXsMFEBF",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:25.829+09:00",
                "progress": 97.61,
                "stopTime": "2020-02-09 21:49:37.941+09:00"
            },
            {
                "clientID": "resnet50_SwfdwwOe9Ete9FTN",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:28.216+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:55.524+09:00"
            },
            {
                "clientID": "inception4_cLpynJ29qz8vJmz1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:38.072+09:00",
                "progress": 98.64,
                "stopTime": "2020-02-09 22:07:35.784+09:00"
            },
            {
                "clientID": "dcgan_CEsvmL97rJbZUf4N",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:45.034+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:17:53.397+09:00"
            },
            {
                "clientID": "googlenet_MG69i37tDJ2idrYw",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:11.563+09:00",
                "progress": 50.0,
                "stopTime": "2020-02-09 21:26:51.848+09:00"
            },
            {
                "clientID": "dcgan_gNY7MtfVGS4sWTAB",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:00.909+09:00",
                "progress": 99.27,
                "stopTime": "2020-02-09 21:19:38.116+09:00"
            },
            {
                "clientID": "vgg16_L5nYfB7qSoMCnGQc",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:44.758+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:49:48.638+09:00"
            },
            {
                "clientID": "video_Mg600ZVeUwK2cVG1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:31.029+09:00",
                "progress": 99.33,
                "stopTime": "2020-02-09 21:46:48.265+09:00"
            },
            {
                "clientID": "inception4_nbUXRf7ZC0mrXn6m",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:46.369+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:34:07.683+09:00"
            },
            {
                "clientID": "dcgan_YxZM7Jq6xP3FerXd",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:47.344+09:00",
                "progress": 99.69,
                "stopTime": "2020-02-09 21:24:12.893+09:00"
            },
            {
                "clientID": "inception4_Seks7seTfEfiNGf1",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:05.715+09:00",
                "progress": 99.51,
                "stopTime": "2020-02-09 22:16:08.474+09:00"
            },
            {
                "clientID": "dcgan_2UYuFFGpqbpEn6je",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:49.755+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:17:45.357+09:00"
            },
            {
                "clientID": "resnet50_8MGZ25liThU3vkXz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:31.294+09:00",
                "progress": 99.89,
                "stopTime": "2020-02-09 21:42:49.440+09:00"
            },
            {
                "clientID": "inception4_Pb7bKACtL2kDPcOv",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:51.498+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 22:20:56.235+09:00"
            },
            {
                "clientID": "dcgan_oDEMoPHXc2cFvcDS",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:48.502+09:00",
                "progress": 99.85,
                "stopTime": "2020-02-09 21:21:19.589+09:00"
            },
            {
                "clientID": "inception4_vk3Dko4IQAAr1HSg",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:42.558+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:01:04.841+09:00"
            },
            {
                "clientID": "googlenet_tm1VVj72ErqGfb6s",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:24.209+09:00",
                "progress": 99.38,
                "stopTime": "2020-02-09 21:28:32.972+09:00"
            },
            {
                "clientID": "vgg16_9l5HTMbumhRIjIsC",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:04.571+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:41.146+09:00"
            },
            {
                "clientID": "dcgan_lYseWmtsCazn5YKr",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:49.952+09:00",
                "progress": 99.94,
                "stopTime": "2020-02-09 21:24:50.732+09:00"
            },
            {
                "clientID": "dcgan_hmGpfDL5XjhucWIE",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:28.752+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:18:35.493+09:00"
            },
            {
                "clientID": "inception4_XVBnq57eEet5RBXW",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:58.265+09:00",
                "progress": 99.59,
                "stopTime": "2020-02-09 22:19:39.607+09:00"
            },
            {
                "clientID": "video_GgM3VQu93ccgm5Um",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:42.616+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:46:23.311+09:00"
            },
            {
                "clientID": "resnet50_ZdLI5jIO1lriFuSU",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:42.044+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:42:00.470+09:00"
            },
            {
                "clientID": "chatbot_CVN7zxrTVu7sNYlI",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:34.446+09:00",
                "progress": 98.41,
                "stopTime": "2020-02-09 21:15:50.117+09:00"
            },
            {
                "clientID": "googlenet_u318sTPOXvJaEbIq",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:09.836+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:26:43.006+09:00"
            },
            {
                "clientID": "googlenet_WKLc3wcE8ZwZsU5S",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:55.675+09:00",
                "progress": 99.91,
                "stopTime": "2020-02-09 21:27:59.512+09:00"
            },
            {
                "clientID": "video_iSDkoD6Yl49rNEJF",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:14.678+09:00",
                "progress": 99.53,
                "stopTime": "2020-02-09 21:39:49.386+09:00"
            },
            {
                "clientID": "video_dpg8nvkIwQTX5x8l",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:44.614+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:43:31.879+09:00"
            },
            {
                "clientID": "chatbot_WGXlu0vv3dQykkoI",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:22.358+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:15:49.305+09:00"
            },
            {
                "clientID": "inception4_8Vp3bepK1LoqE7tS",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:45.505+09:00",
                "progress": 96.87,
                "stopTime": "2020-02-09 22:06:50.164+09:00"
            },
            {
                "clientID": "chatbot_WzWV5aLjnYNFUmX4",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:33.161+09:00",
                "progress": 99.31,
                "stopTime": "2020-02-09 21:18:04.026+09:00"
            },
            {
                "clientID": "chatbot_hUzuqEpud0WcfIOE",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:17.828+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:54.452+09:00"
            },
            {
                "clientID": "inception4_pXXxFESPY0oQVzYG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:31.145+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 22:17:33.109+09:00"
            },
            {
                "clientID": "video_BkCcvupoa7ats3wo",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:04.844+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:44:17.936+09:00"
            },
            {
                "clientID": "dcgan_37NgKNs81eHNHg3S",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:47.200+09:00",
                "progress": 99.65,
                "stopTime": "2020-02-09 21:21:55.332+09:00"
            },
            {
                "clientID": "vgg16_De7PIBTt0aLQ6RAb",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:31.614+09:00",
                "progress": 97.5,
                "stopTime": "2020-02-09 21:50:21.751+09:00"
            },
            {
                "clientID": "vgg16_odu8TAAtdLIz9OjM",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:25.334+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:59:19.500+09:00"
            },
            {
                "clientID": "resnet50_Px5ARDQ5oewJNNhw",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:34.922+09:00",
                "progress": 99.77,
                "stopTime": "2020-02-09 21:42:40.513+09:00"
            },
            {
                "clientID": "chatbot_nFKgejaxwUzNsQjf",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:28.201+09:00",
                "progress": 98.5,
                "stopTime": "2020-02-09 21:16:26.094+09:00"
            },
            {
                "clientID": "googlenet_APsGoN2loFWBYUWv",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:35.496+09:00",
                "progress": 99.85,
                "stopTime": "2020-02-09 21:28:01.442+09:00"
            },
            {
                "clientID": "googlenet_95ZRW3iZEOsi1agM",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:11.153+09:00",
                "progress": 66.66,
                "stopTime": "2020-02-09 21:26:40.326+09:00"
            },
            {
                "clientID": "dcgan_4x3Cs60QGSYeDq7O",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:25.845+09:00",
                "progress": 99.02,
                "stopTime": "2020-02-09 21:18:35.156+09:00"
            },
            {
                "clientID": "video_ys8YbPjhnuOP9NuY",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:56.239+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:40:35.774+09:00"
            },
            {
                "clientID": "dcgan_KoxUncx427xz5EO0",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:54.213+09:00",
                "progress": 99.8,
                "stopTime": "2020-02-09 21:22:06.989+09:00"
            },
            {
                "clientID": "video_zYDA1I5cprLT4Sr6",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:26.312+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:45:41.883+09:00"
            },
            {
                "clientID": "googlenet_o524kS3lttJJJ1DV",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:07.409+09:00",
                "progress": 99.6,
                "stopTime": "2020-02-09 21:28:41.060+09:00"
            },
            {
                "clientID": "resnet50_9awGTpyd6bUT3xni",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:01.529+09:00",
                "progress": 99.65,
                "stopTime": "2020-02-09 21:33:32.715+09:00"
            },
            {
                "clientID": "chatbot_1bOODTzxAMmkH9GX",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:58.985+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:15:32.528+09:00"
            },
            {
                "clientID": "googlenet_fCwvVIANt53yXeUH",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:46.690+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:26:29.067+09:00"
            },
            {
                "clientID": "chatbot_06SWGU6BFQVlLcAv",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:33.454+09:00",
                "progress": 99.55,
                "stopTime": "2020-02-09 21:16:59.435+09:00"
            },
            {
                "clientID": "resnet50_o5ntacbhKC2uC6hG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:22.409+09:00",
                "progress": 99.59,
                "stopTime": "2020-02-09 21:34:58.162+09:00"
            },
            {
                "clientID": "googlenet_8yk7gnn3EGJgzdb8",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:49.897+09:00",
                "progress": 99.75,
                "stopTime": "2020-02-09 21:32:18.701+09:00"
            },
            {
                "clientID": "dcgan_e9vNK5fgZ8rSYBtj",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:09.799+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:17:48.015+09:00"
            },
            {
                "clientID": "googlenet_LP3epTwG85vB8rhQ",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:01.750+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:28:41.721+09:00"
            },
            {
                "clientID": "inception4_3zG1WpMuPlfbFvmz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:03.088+09:00",
                "progress": 99.5,
                "stopTime": "2020-02-09 22:14:43.266+09:00"
            },
            {
                "clientID": "googlenet_2br8jDRbZna4ot1H",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:14.249+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:27:02.937+09:00"
            },
            {
                "clientID": "inception4_WfcnQm0wf39IAeO9",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:43.860+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:36:12.881+09:00"
            },
            {
                "clientID": "video_skjbzJhFJFANWv7p",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:44.518+09:00",
                "progress": 99.57,
                "stopTime": "2020-02-09 21:47:19.562+09:00"
            },
            {
                "clientID": "googlenet_cwyO4kKIAK1vU4ta",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:31.378+09:00",
                "progress": 99.75,
                "stopTime": "2020-02-09 21:27:16.051+09:00"
            },
            {
                "clientID": "video_jyhpmKcFhh4MhhCJ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:23.391+09:00",
                "progress": 99.01,
                "stopTime": "2020-02-09 21:46:52.770+09:00"
            },
            {
                "clientID": "video_5AXX4SikOc1nQv4T",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:18.331+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:46:56.270+09:00"
            },
            {
                "clientID": "vgg16_VGtSYsLbf5HJoLH2",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:26.788+09:00",
                "progress": 99.6,
                "stopTime": "2020-02-09 21:58:55.342+09:00"
            },
            {
                "clientID": "chatbot_K2esqpC0J1usSjQG",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:04.427+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:16:26.271+09:00"
            },
            {
                "clientID": "chatbot_XPNztJf0eLaDFGgE",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:00.836+09:00",
                "progress": 50.0,
                "stopTime": "2020-02-09 21:15:32.178+09:00"
            },
            {
                "clientID": "video_ByRFTUrxcmNGkkCC",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:04.187+09:00",
                "progress": 99.67,
                "stopTime": "2020-02-09 21:46:26.380+09:00"
            },
            {
                "clientID": "video_BqbxmNZmlFlL2itq",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:51.224+09:00",
                "progress": 99.56,
                "stopTime": "2020-02-09 21:47:30.836+09:00"
            },
            {
                "clientID": "vgg16_B6gYXPo0xU6PaXi9",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:38.434+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:49:06.086+09:00"
            },
            {
                "clientID": "video_SzNZkqLnNssbQPdt",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:16.546+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:45:13.761+09:00"
            },
            {
                "clientID": "dcgan_pCbWL2HVlUAMj59r",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:53.412+09:00",
                "progress": 99.92,
                "stopTime": "2020-02-09 21:21:29.092+09:00"
            },
            {
                "clientID": "vgg16_D3ZAPTQXsFpcbOCs",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:02.139+09:00",
                "progress": 98.78,
                "stopTime": "2020-02-09 21:51:03.607+09:00"
            },
            {
                "clientID": "video_1wzdqwggds4BQd3n",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:26.531+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:47:48.277+09:00"
            },
            {
                "clientID": "vgg16_vxbQI96O1on99mfW",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:34.460+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:48:39.691+09:00"
            },
            {
                "clientID": "vgg16_YiXibDd06F734H9o",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:48.868+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:50:10.232+09:00"
            },
            {
                "clientID": "chatbot_Nnt8HKF8eGmP3DC5",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:04.687+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:20.242+09:00"
            },
            {
                "clientID": "video_nWtGkBwNLmg0yMxn",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:16.859+09:00",
                "progress": 99.27,
                "stopTime": "2020-02-09 21:41:32.735+09:00"
            },
            {
                "clientID": "resnet50_llmnbOB8vIRe1vsU",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:01.017+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:20.047+09:00"
            },
            {
                "clientID": "inception4_NDxJDynFmJE1j8Jl",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:21.096+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 22:16:20.144+09:00"
            },
            {
                "clientID": "googlenet_gAHAUSZrZjcjGJXw",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:00.273+09:00",
                "progress": 40.0,
                "stopTime": "2020-02-09 21:26:30.876+09:00"
            },
            {
                "clientID": "vgg16_hmVSTwkFn2c2V85F",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:12.285+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:51:00.177+09:00"
            },
            {
                "clientID": "resnet50_ekN6azPtiCOCF27i",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:36.240+09:00",
                "progress": 88.88,
                "stopTime": "2020-02-09 21:31:01.482+09:00"
            },
            {
                "clientID": "inception4_mZzVtojHg9xzJo9M",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:22.503+09:00",
                "progress": 99.06,
                "stopTime": "2020-02-09 22:11:17.311+09:00"
            },
            {
                "clientID": "resnet50_MmSmWndllaN01dfA",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:47.248+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:41:01.506+09:00"
            },
            {
                "clientID": "chatbot_bqMUeMgyugXh8ZL7",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:25.744+09:00",
                "progress": 97.88,
                "stopTime": "2020-02-09 21:16:06.096+09:00"
            },
            {
                "clientID": "resnet50_TgMGZi53lR7vNozk",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:37.041+09:00",
                "progress": 98.95,
                "stopTime": "2020-02-09 21:33:03.386+09:00"
            },
            {
                "clientID": "googlenet_0xOOEa9rzEnG7ymu",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:32.837+09:00",
                "progress": 99.09,
                "stopTime": "2020-02-09 21:27:26.011+09:00"
            },
            {
                "clientID": "googlenet_LZ8l84FCLBOeLJjd",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:04.642+09:00",
                "progress": 99.87,
                "stopTime": "2020-02-09 21:32:18.004+09:00"
            },
            {
                "clientID": "chatbot_wcAvz65uhLEcwK9l",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:07.500+09:00",
                "progress": 98.74,
                "stopTime": "2020-02-09 21:16:14.163+09:00"
            },
            {
                "clientID": "vgg16_04uwIZd0BwIqrN2P",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:01.574+09:00",
                "progress": 99.11,
                "stopTime": "2020-02-09 21:53:00.386+09:00"
            },
            {
                "clientID": "inception4_i0ycpq6dhCAqb7xR",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:34.592+09:00",
                "progress": 99.59,
                "stopTime": "2020-02-09 22:14:17.534+09:00"
            },
            {
                "clientID": "chatbot_JlpzBAas2x3lSxwh",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:21.000+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:43.183+09:00"
            },
            {
                "clientID": "video_9JjvFm0M28vxDDGH",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:24.045+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:47:36.943+09:00"
            },
            {
                "clientID": "vgg16_LJL0OESJHxHEuj88",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:31.398+09:00",
                "progress": 97.29,
                "stopTime": "2020-02-09 21:49:57.639+09:00"
            },
            {
                "clientID": "googlenet_MCMVpSB2MdjKkqdK",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:49.808+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:26:27.079+09:00"
            },
            {
                "clientID": "resnet50_u2NwLfZfpbvyl3JS",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:46.557+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:36:33.738+09:00"
            },
            {
                "clientID": "chatbot_qlmykyTOHmxJaRcM",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:54.297+09:00",
                "progress": 97.51,
                "stopTime": "2020-02-09 21:16:18.557+09:00"
            },
            {
                "clientID": "chatbot_FIuyJ5PNcFQJ1LGG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:35.753+09:00",
                "progress": 99.28,
                "stopTime": "2020-02-09 21:18:14.766+09:00"
            },
            {
                "clientID": "video_gjz3R4PoMVKgFQhf",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:43.626+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:45:24.697+09:00"
            },
            {
                "clientID": "inception4_0ensosXUkGMnQLyh",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:03.874+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:07:13.855+09:00"
            },
            {
                "clientID": "resnet50_UYmcxvZEIGDA8RZf",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:12.224+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:33:55.527+09:00"
            },
            {
                "clientID": "googlenet_R296zzLWktppvHvx",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:32.993+09:00",
                "progress": 99.87,
                "stopTime": "2020-02-09 21:33:46.718+09:00"
            },
            {
                "clientID": "inception4_9hSc9jiCeb7ugUSA",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:17.569+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:07:52.635+09:00"
            },
            {
                "clientID": "googlenet_1Xu1mNsJTBPqXUzH",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:14.813+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 21:28:01.792+09:00"
            },
            {
                "clientID": "inception4_tGb71UmWRri1hZPf",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:05.867+09:00",
                "progress": 99.27,
                "stopTime": "2020-02-09 22:10:19.825+09:00"
            },
            {
                "clientID": "video_JMKVgPQlBBFdv03A",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:29.309+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:47:40.106+09:00"
            },
            {
                "clientID": "inception4_r1o4YoNtggi0WCEe",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:42.913+09:00",
                "progress": 98.07,
                "stopTime": "2020-02-09 22:07:25.476+09:00"
            },
            {
                "clientID": "resnet50_pWlTBUWTLecRaCub",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:03.233+09:00",
                "progress": 99.56,
                "stopTime": "2020-02-09 21:32:49.591+09:00"
            },
            {
                "clientID": "inception4_v2nXZs2yXXtAQSyX",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:52.009+09:00",
                "progress": 99.54,
                "stopTime": "2020-02-09 22:16:54.117+09:00"
            },
            {
                "clientID": "video_o7HJXNlUttq2ugmT",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:00.223+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:44:08.949+09:00"
            },
            {
                "clientID": "chatbot_T1Ebq0401GsRmXnY",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:38.894+09:00",
                "progress": 99.49,
                "stopTime": "2020-02-09 21:17:41.617+09:00"
            },
            {
                "clientID": "video_zJxluPsbfsfOm3Rm",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:21.521+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:44:33.587+09:00"
            },
            {
                "clientID": "vgg16_vk5XHfrlFVhRulbB",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:27.786+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:51:01.466+09:00"
            },
            {
                "clientID": "resnet50_ci0U6QUgQ1a1Pzcf",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:59.962+09:00",
                "progress": 99.89,
                "stopTime": "2020-02-09 21:42:53.588+09:00"
            },
            {
                "clientID": "vgg16_Z89UlMt6u92xQLyk",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:27.012+09:00",
                "progress": 99.43,
                "stopTime": "2020-02-09 21:55:00.579+09:00"
            },
            {
                "clientID": "chatbot_n18j4nwSBj8wxq53",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:20.518+09:00",
                "progress": 99.26,
                "stopTime": "2020-02-09 21:16:17.334+09:00"
            },
            {
                "clientID": "resnet50_qbig3dG6g9h4YCwD",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:09.472+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:35:08.835+09:00"
            },
            {
                "clientID": "inception4_16HUoeXFb3LcDheW",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:41.425+09:00",
                "progress": 99.76,
                "stopTime": "2020-02-09 22:35:25.003+09:00"
            },
            {
                "clientID": "video_bOpxHXTp1ttEKvaR",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:31.605+09:00",
                "progress": 98.6,
                "stopTime": "2020-02-09 21:46:48.599+09:00"
            },
            {
                "clientID": "inception4_jjylnk9x4WC8bwHU",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:58.764+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:06:00.602+09:00"
            },
            {
                "clientID": "chatbot_5P71Gq63ynklXJnP",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:38.801+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:15:49.299+09:00"
            },
            {
                "clientID": "video_doMqZBDns1OKZkMG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:29.570+09:00",
                "progress": 98.55,
                "stopTime": "2020-02-09 21:47:15.189+09:00"
            },
            {
                "clientID": "chatbot_MUTl9P266BHwSKIA",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:19.129+09:00",
                "progress": 98.56,
                "stopTime": "2020-02-09 21:15:39.968+09:00"
            },
            {
                "clientID": "inception4_ozeXFWmTFRHjFtJQ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:40.672+09:00",
                "progress": 97.95,
                "stopTime": "2020-02-09 22:05:10.772+09:00"
            },
            {
                "clientID": "video_0h7oAa4Ru3oampJ6",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:44.795+09:00",
                "progress": 99.58,
                "stopTime": "2020-02-09 21:48:06.533+09:00"
            },
            {
                "clientID": "video_29DXyfYIsWji95zg",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:43.381+09:00",
                "progress": 99.62,
                "stopTime": "2020-02-09 21:42:22.742+09:00"
            },
            {
                "clientID": "resnet50_t0NaLcx5Uh6cjrD8",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:04.867+09:00",
                "progress": 99.62,
                "stopTime": "2020-02-09 21:36:00.676+09:00"
            },
            {
                "clientID": "googlenet_Jk1Z4VSbXjxYRFdC",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:37.002+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:25:26.113+09:00"
            },
            {
                "clientID": "vgg16_MhwvfWOPH6nQnWAY",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:44.334+09:00",
                "progress": 99.29,
                "stopTime": "2020-02-09 21:53:58.357+09:00"
            },
            {
                "clientID": "resnet50_APbSxQ0hqLNi1rAt",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:34.524+09:00",
                "progress": 99.01,
                "stopTime": "2020-02-09 21:32:28.338+09:00"
            },
            {
                "clientID": "vgg16_Tn6z175hdN6qtXLD",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:04.609+09:00",
                "progress": 99.26,
                "stopTime": "2020-02-09 21:53:11.064+09:00"
            },
            {
                "clientID": "googlenet_vzYGwHJldfPlyg05",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:00.208+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:26:12.881+09:00"
            },
            {
                "clientID": "googlenet_JU9qoi1xxrQTNw7G",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:49.546+09:00",
                "progress": 99.79,
                "stopTime": "2020-02-09 21:29:04.092+09:00"
            },
            {
                "clientID": "vgg16_wxV06ekuozJvfbTC",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:42.005+09:00",
                "progress": 98.8,
                "stopTime": "2020-02-09 21:50:58.086+09:00"
            },
            {
                "clientID": "resnet50_5VcQaZ2v7t2iyJfS",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:19.600+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:42.410+09:00"
            },
            {
                "clientID": "inception4_VD3PYQrYoCRL5Our",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:51.785+09:00",
                "progress": 99.62,
                "stopTime": "2020-02-09 22:22:20.425+09:00"
            },
            {
                "clientID": "resnet50_Iw8JkUB71a3rSJNe",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:32.363+09:00",
                "progress": 99.77,
                "stopTime": "2020-02-09 21:42:15.166+09:00"
            },
            {
                "clientID": "resnet50_dERlbGOyZLJHcLoa",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:33.517+09:00",
                "progress": 99.89,
                "stopTime": "2020-02-09 21:43:07.541+09:00"
            },
            {
                "clientID": "inception4_7IrW2XZ2x0RA3vOc",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:04.664+09:00",
                "progress": 99.51,
                "stopTime": "2020-02-09 22:16:52.577+09:00"
            },
            {
                "clientID": "inception4_PTvh2RCRu3b43mzK",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:11.114+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:06:48.225+09:00"
            },
            {
                "clientID": "video_13fJw9ZCOVpy8UUr",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:32.683+09:00",
                "progress": 98.34,
                "stopTime": "2020-02-09 21:46:17.130+09:00"
            },
            {
                "clientID": "vgg16_FHDnr305qTGJJwRo",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:23.686+09:00",
                "progress": 99.55,
                "stopTime": "2020-02-09 21:57:48.430+09:00"
            },
            {
                "clientID": "vgg16_sljET9nW17duJ2q0",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:12:49.363+09:00",
                "progress": 99.61,
                "stopTime": "2020-02-09 21:58:40.998+09:00"
            },
            {
                "clientID": "video_hNOLjfoR1A3UoIWy",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:17.604+09:00",
                "progress": 99.57,
                "stopTime": "2020-02-09 21:43:42.307+09:00"
            },
            {
                "clientID": "resnet50_VZgENW6jRpVGURFa",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:02.884+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:33:23.971+09:00"
            },
            {
                "clientID": "chatbot_I5qZZpM1dcNnc9bQ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:13.873+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:16:15.551+09:00"
            },
            {
                "clientID": "resnet50_XYRAKGcjTQPqn08Z",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:13:49.961+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:39:52.460+09:00"
            },
            {
                "clientID": "inception4_15FCrr7nJNfuaI0M",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:55.957+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:05:24.338+09:00"
            },
            {
                "clientID": "dcgan_ma81TkJq7D541RNj",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:44.782+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:17:37.329+09:00"
            },
            {
                "clientID": "dcgan_BYYkiEpH9Rb6hb5G",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:40.435+09:00",
                "progress": -1,
                "stopTime": "2020-02-09 21:17:27.401+09:00"
            },
            {
                "clientID": "chatbot_d3WOG3VrtNSA83hV",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:17.778+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:15:47.353+09:00"
            },
            {
                "clientID": "video_TwiAWIstSdwKsluw",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:31.881+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:46:26.321+09:00"
            },
            {
                "clientID": "video_aXtkcegirOZunW5C",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:20.812+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:42:00.467+09:00"
            },
            {
                "clientID": "googlenet_25gBj3vkO1TiBRM2",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:04.300+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:26:31.196+09:00"
            },
            {
                "clientID": "googlenet_m3Da3COCvJbZNwKv",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:05.026+09:00",
                "progress": 99.68,
                "stopTime": "2020-02-09 21:27:46.558+09:00"
            },
            {
                "clientID": "resnet50_nIEnvEzCMyyd40mF",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:48.623+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:33:01.819+09:00"
            },
            {
                "clientID": "chatbot_JWEH3hitd7OJhRw3",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:13.829+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:16:17.544+09:00"
            },
            {
                "clientID": "dcgan_OgJxlOkKQtOVKxtF",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:31.412+09:00",
                "progress": 98.58,
                "stopTime": "2020-02-09 21:19:22.670+09:00"
            },
            {
                "clientID": "resnet50_wKzSilwTAmk5ZkeF",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:37.848+09:00",
                "progress": 99.88,
                "stopTime": "2020-02-09 21:42:08.373+09:00"
            },
            {
                "clientID": "resnet50_D1c4wNpXWr2f0plV",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:32.211+09:00",
                "progress": 99.89,
                "stopTime": "2020-02-09 21:42:33.781+09:00"
            },
            {
                "clientID": "vgg16_If6uInY0vc88XFiy",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:25.980+09:00",
                "progress": 99.4,
                "stopTime": "2020-02-09 21:54:46.435+09:00"
            },
            {
                "clientID": "vgg16_yr9xvZC0u3LRIOfR",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:57.410+09:00",
                "progress": 99.23,
                "stopTime": "2020-02-09 21:53:43.624+09:00"
            },
            {
                "clientID": "googlenet_7xqhkgoVzooIrqeF",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:46.895+09:00",
                "progress": 99.65,
                "stopTime": "2020-02-09 21:27:24.233+09:00"
            },
            {
                "clientID": "video_3AdaRX0XDkndU3np",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:21.655+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:45:25.371+09:00"
            },
            {
                "clientID": "dcgan_Dg5WT8ydvXVVfHfJ",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:12.758+09:00",
                "progress": -1,
                "stopTime": "2020-02-09 21:17:54.907+09:00"
            },
            {
                "clientID": "inception4_9LtYdE9Im6aQwICa",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:04.588+09:00",
                "progress": 99.56,
                "stopTime": "2020-02-09 22:14:45.044+09:00"
            },
            {
                "clientID": "dcgan_oucUi5aQwG44kZz5",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:05.899+09:00",
                "progress": 99.6,
                "stopTime": "2020-02-09 21:20:36.262+09:00"
            },
            {
                "clientID": "vgg16_6aO1d4enrhMcW9VS",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:58.147+09:00",
                "progress": 98.7,
                "stopTime": "2020-02-09 21:51:16.710+09:00"
            },
            {
                "clientID": "dcgan_Zk8qgAjGo6PPXIEn",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:14:48.772+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:17:41.580+09:00"
            },
            {
                "clientID": "googlenet_lYEKql5QoNYIvS0X",
                "clientGPUList": {},
                "status": "Completed",
                "startTime": "2020-02-09 21:15:12.827+09:00",
                "progress": 100.0,
                "stopTime": "2020-02-09 21:27:01.127+09:00"
            },
            {
                "clientID": "dcgan_1sfH60HlI4taeCJX",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:44.999+09:00",
                "progress": 33.33,
                "stopTime": "2020-02-09 21:17:36.235+09:00"
            },
            {
                "clientID": "dcgan_QJRaNxNFTxgPpP8V",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:59.651+09:00",
                "progress": 99.59,
                "stopTime": "2020-02-09 21:21:44.771+09:00"
            },
            {
                "clientID": "vgg16_TzthHaqLTFJIF5M8",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:38.478+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:49:15.127+09:00"
            },
            {
                "clientID": "googlenet_Q8Lj0QI22qqQYqV5",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:13.940+09:00",
                "progress": 99.95,
                "stopTime": "2020-02-09 21:33:35.708+09:00"
            },
            {
                "clientID": "chatbot_Jr2QtGJEyB3GPBgz",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:13.189+09:00",
                "progress": 96.56,
                "stopTime": "2020-02-09 21:16:32.700+09:00"
            },
            {
                "clientID": "inception4_SHutcIX2WlWrnZNG",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:25.178+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 22:08:38.191+09:00"
            },
            {
                "clientID": "vgg16_MEEfI2oBsNrQOeuU",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:13:31.182+09:00",
                "progress": 99.6,
                "stopTime": "2020-02-09 21:58:55.651+09:00"
            },
            {
                "clientID": "video_jLuV027wrRWKcP13",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:15:10.966+09:00",
                "progress": 0.0,
                "stopTime": "2020-02-09 21:46:07.132+09:00"
            },
            {
                "clientID": "googlenet_j4lNsEbZRtB9X8gT",
                "clientGPUList": {},
                "status": "Killed",
                "startTime": "2020-02-09 21:14:29.200+09:00",
                "progress": 99.32,
                "stopTime": "2020-02-09 21:26:31.842+09:00"
            }
        ]
    }
}
]

def time_str2stamp(tstr):
    day, hour = tstr.split(' ')
    d = int(day.split('-')[-1]) * 3600 * 24
    hour = hour.split('+')[0]
    h, m, s = hour.split(':')
    h = 3600 * int(h)
    m = 60 * int(m)
    s = float(s)
    return d + h + m + s

fig, [ax_act, ax_qlen, ax_msoj, ax_util] = plt.subplots(1, 4, sharex=False)
num_gpus = 1
max_act = 0
last_time = 0
prog_data_ctime_list = []
prog_data_act_list = []
prog_data_qlen_list = []
prog_data_msoj_list = []
prog_data_util_list = []

prog_data_list = []
for trace in traces:
    timeline = []
    for c in trace['TotalUserinfo']['ClientInfo']:
        timeline.append([time_str2stamp(c['startTime']), c['clientID'], True])
        timeline.append([time_str2stamp(c['stopTime']), c['clientID'], False])
    timeline.sort()
    mintime = timeline[0][0]
    for x in timeline:
        x[0] -= mintime

    unfins = []
    fins = []
    prog_data = []

    def act(ts):
        n = len(fins) + len(unfins)
        if n == 0:
            return 0
        sct = 0
        if len(fins) > 0:
            sct += sum(fins)
        if len(unfins) > 0:
            sct += sum([ts - t for t, _ in unfins])
        return sct / n

    def msoj(ts):
        if len(unfins) == 0:
            return 0
        return ts - min([t for t, _ in unfins])

    for ts, cid, is_start in sorted(timeline):
        prog_data.append((ts, act(ts), len(unfins), msoj(ts), 0))
        if is_start:
            unfins.append((ts, cid))
        else:
            for i, (start, c) in enumerate(unfins):
                if c == cid:
                    fins.append(ts - start)
                    break
            del unfins[i]
        prog_data.append((ts, act(ts), len(unfins), msoj(ts), 0))
    prog_data_list.append(prog_data)

for prog_data in prog_data_list:
    # ret, prog_data = run_sim(a, num_gpus, tr.trace)
    # rets.append(ret)
    prog_data_ctime = []
    prog_data_act = []
    prog_data_qlen = []
    prog_data_msoj = []
    prog_data_util = []
    for ctime, act, qlen, msoj, util in prog_data:
        prog_data_ctime.append(ctime/60.)
        prog_data_act.append(act/60.)
        prog_data_qlen.append(qlen)
        prog_data_msoj.append(msoj/60.)
        prog_data_util.append(util/num_gpus*100.)
        max_act = max(max_act, prog_data_act[-1])
    prog_data_ctime_list.append(prog_data_ctime)
    prog_data_act_list.append(prog_data_act)
    prog_data_qlen_list.append(prog_data_qlen)
    prog_data_msoj_list.append(prog_data_msoj)
    prog_data_util_list.append(prog_data_util)
    last_time = max(last_time, prog_data_ctime[-1])
for i in range(len(prog_data_list)):
    prog_data_ctime_list[i].append(last_time * 1.03)
    prog_data_act_list[i].append(prog_data_act_list[i][-1])
    prog_data_qlen_list[i].append(prog_data_qlen_list[i][-1])
    prog_data_msoj_list[i].append(prog_data_msoj_list[i][-1])
    prog_data_util_list[i].append(prog_data_util_list[i][-1])
    ax_act.plot(prog_data_ctime_list[i], prog_data_act_list[i], label=i)
    ax_qlen.plot(prog_data_ctime_list[i], prog_data_qlen_list[i], label=i)
    ax_msoj.plot(prog_data_ctime_list[i], prog_data_msoj_list[i], label=i)
    ax_util.plot(prog_data_ctime_list[i], prog_data_util_list[i], label=i)

plot_show(fig, (ax_act, ax_qlen, ax_msoj, ax_util))
with io.open('plot_real_%d.pkl' % time.time(), 'wb') as f:
    pickle.dump((ax_act, ax_qlen, ax_msoj, ax_util), f)
with io.open('plot_real_latest.pkl', 'wb') as f:
    pickle.dump((ax_act, ax_qlen, ax_msoj, ax_util), f)