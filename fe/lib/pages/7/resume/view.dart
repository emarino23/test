import 'package:flutter/material.dart';
import 'package:naver_crs/index.dart';
import 'package:get/get.dart';
import 'package:sweetalertv2/sweetalertv2.dart';
import 'widgets/index.dart';

class ResumePage extends GetView<ResumeController> {
  ResumePage({Key? key}) : super(key: key);

  final Map<String, GlobalKey<State<StatefulWidget>>> keys = {
    "cover": GlobalKey(),
    "header": GlobalKey(),
    "dest": GlobalKey(),
    "end": GlobalKey()
  };

  Widget _buildView(BuildContext _context) {
    return ContentLayoutWidget(
        background: "assets/images/1x/resume.png",
        child: Stack(
          children: [
            ResumeWidget(pkeys: keys),
          ],
        ),
        text: '');
  }

  final _controller = ScrollController();
  @override
  Widget build(BuildContext context) {
    var guides = getGuides();
    return WillPopScope(
      onWillPop: () async => false,
      child: Scaffold(
        floatingActionButton: Stack(
          children: [
            Positioned(
              left: Get.width * 0.92,
              top: Get.height * 0.5,
              child: ScrollTopDownArrows(controller: _controller),
            ),
            FloatingActionButton(
              onPressed: () async {
                if (guides == 0) {
                  SweetAlertV2.show(context,
                      curve: ElasticInCurve(),
                      title: "Do you Want to take a Guide?",
                      style: SweetAlertV2Style.confirm,
                      cancelButtonText: "No",
                      cancelButtonColor: Colors.red,
                      confirmButtonColor: Colors.green,
                      confirmButtonText: "Yes",
                      showCancelButton: true, onPress: (bool isConfirm) {
                    if (isConfirm) {
                      Get.close(1);
                    } else {
                      guides = 1;
                      Get.close(1);
                    }

                    return false;
                  });
                } else {
                  SweetAlertV2.show(context,
                      curve: ElasticInCurve(),
                      title: "Do you Want to send Tour?",
                      style: SweetAlertV2Style.confirm,
                      cancelButtonText: "No",
                      cancelButtonColor: Colors.red,
                      confirmButtonColor: Colors.green,
                      confirmButtonText: "Yes",
                      showCancelButton: true, onPress: (bool isConfirm) {
                    if (isConfirm) {
                      (() async {
                        await processTour();
                      })();
                      Get.close(1);
                    } else {
                      Get.close(1);
                    }
                    return false;
                  });
                }
              },
              child: Icon(Icons.save),
              backgroundColor: Colors.green,
            ),
          ],
        ),
        body: Scrollbar(
            child: SingleChildScrollView(
          controller: _controller,
          child: SizedBox(
              width: Get.width,
              height: Get.height * 2,
              child: _buildView(context)),
        )),
        bottomNavigationBar: NavBarWidget(),
      ),
    );
  }
}
