import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Subcat3Component } from './subcat3.component';

describe('Subcat3Component', () => {
  let component: Subcat3Component;
  let fixture: ComponentFixture<Subcat3Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Subcat3Component ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(Subcat3Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
