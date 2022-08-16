part of './app_pages.dart';

class PRegistry {
  PRegistry({this.name, this.page, this.transition, this.binding});
  final String? name;
  final dynamic page;
  final dynamic transition;
  final dynamic binding;
}

List<dynamic> routes = [
  PRegistry(
      name: '/Splash',
      page: SplashPage(),
      transition: Transition.zoom,
      binding: SplashBinding()),
  PRegistry(
      name: '/Signin',
      page: SigninPage(),
      transition: Transition.zoom,
      binding: SigninBinding()),
  PRegistry(
      name: '/Forgot',
      page: ForgotPage(),
      transition: Transition.zoom,
      binding: ForgotBinding()),
  PRegistry(
      name: '/Loading',
      page: LoadingPage(),
      transition: Transition.zoom,
      binding: LoadingBinding()),
  PRegistry(
      name: '/Tour',
      page: TourPage(),
      transition: Transition.zoom,
      binding: TourBinding()),
  PRegistry(
      name: '/Logistic',
      page: LogisticPage(),
      transition: Transition.zoom,
      binding: LogisticBinding()),
  PRegistry(
      name: '/Customer',
      page: CustomerPage(),
      transition: Transition.zoom,
      binding: CustomerBinding()),
  PRegistry(
      name: '/Destination',
      page: DestinationPage(),
      transition: Transition.zoom,
      binding: DestinationBinding()),
  PRegistry(
      name: '/Experiences',
      page: ExperiencesPage(),
      transition: Transition.zoom,
      binding: ExperiencesBinding()),
  PRegistry(
      name: '/Resume',
      page: ResumePage(),
      transition: Transition.zoom,
      binding: ResumeBinding()),
  PRegistry(
      name: '/PrintResume',
      page: PrintResumePage(),
      transition: Transition.zoom,
      binding: PrintResumeBinding()),
  PRegistry(
      name: '/NetRate',
      page: NetRatePage(),
      transition: Transition.zoom,
      binding: NetRateBinding()),
  PRegistry(
      name: '/PrintDocs',
      page: PrintDocsPage(),
      transition: Transition.zoom,
      binding: PrintDocsBinding()),
  PRegistry(
      name: '/Services',
      page: ServicesPage(),
      transition: Transition.zoom,
      binding: ServicesBinding()),
  PRegistry(
      name: '/Searcher',
      page: SearcherPage(),
      transition: Transition.zoom,
      binding: SearcherBinding()),
];
