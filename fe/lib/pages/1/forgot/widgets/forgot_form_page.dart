import 'package:flutter/material.dart';
import 'index.dart';
import 'package:naver_crs/index.dart';
import 'package:get/get.dart';

class ForgotFormPage extends GetView<StatelessWidget> {
  ForgotFormPage({
    Key? key,
    this.ctrl,
  }) : super(key: key);
  final _formKey = GlobalKey<FormState>();
  final ForgotController? ctrl;
  @override
  Widget build(BuildContext context) {
    return Center(
      child: SafeArea(
        child: SingleChildScrollView(
          padding: EdgeInsets.symmetric(horizontal: kDefaultPadding),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              ForgotTitle(),
              SizedBox(height: kDefaultPadding * 1),
              ForgotForm(formKey: _formKey, state: ctrl!.state),
              SizedBox(height: kDefaultPadding * 2),
              SizedBox(
                child: RoundedFormButton(
                  height: 0.06,
                  fontSize: 12,
                  color: Color.fromARGB(255, 115, 115, 115),
                  textColor: Colors.white70,
                  fontWeight: FontWeight.bold,
                  label: "Send",
                  onPressed: () {
                    if (_formKey.currentState!.validate()) {
                      _formKey.currentState!.save();
                      ctrl!.onForgot(context, ctrl!.state.email);
                    }
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class ForgotTitle extends StatelessWidget {
  const ForgotTitle({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(
        top: Get.height * 0.05,
        left: Get.width * 0,
      ),
      child: Text(
        'Forgot password?',
        style: KTextSytle(
          context: context,
          fontSize: 25,
          fontWeight: FontWeight.bold,
          color: Color.fromARGB(255, 204, 164, 61),
        ).getStyle(),
      ),
    );
  }
}
