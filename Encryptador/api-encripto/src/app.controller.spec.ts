import { Test, TestingModule } from '@nestjs/testing';
import { AppController } from './app.controller';
import { AppService } from './app.service';

describe('AppController', () => {
  let appController: AppController;

  beforeEach(async () => {
    const app: TestingModule = await Test.createTestingModule({
      controllers: [AppController],
      providers: [AppService],
    }).compile();

    appController = app.get<AppController>(AppController);
  });

  beforeAll(() => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date(2023, 1, 27));
  });

  afterAll(() => {
    jest.useRealTimers();
  });

  describe('root', () => {
    it('should return "Mon Feb 27 2023"', () => {
      expect(appController.getHelathCheck()).toBe('Mon Feb 27 2023');
    });
  });
});
